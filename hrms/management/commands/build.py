import shutil
import yaml
from pathlib import Path

from django.apps import apps
from django.conf import settings
from django.core.management.base import BaseCommand


def collect_operations():
    """Scan installed apps for api_specs/openapi.yaml and yield (app_name, path, method, operation_id)."""
    for app_config in apps.get_app_configs():
        openapi_path = Path(app_config.path) / "api_specs" / "openapi.yaml"
        if not openapi_path.is_file():
            continue
        with open(openapi_path) as f:
            spec = yaml.safe_load(f)
        paths = spec.get("paths") or {}
        for path_pattern, path_item in paths.items():
            if not isinstance(path_item, dict):
                continue
            for method in ("get", "post", "put", "patch", "delete"):
                op = path_item.get(method)
                if not op or not isinstance(op, dict):
                    continue
                operation_id = op.get("operationId")
                if not operation_id:
                    continue
                path_str = path_pattern.strip("/")
                if path_str:
                    path_str += "/"
                else:
                    path_str = ""
                yield (app_config.name, path_str, method, operation_id)


def write_view_file(build_views_dir: Path, app_name: str, operation_id: str, content: str) -> None:
    path = build_views_dir / f"{operation_id}.py"
    path.write_text(content, encoding="utf-8")


def write_urls(build_dir: Path, operations: list) -> None:
    if not operations:
        return
    seen_ids = set()
    import_names = []
    path_entries = []
    for app_name, path_str, method, operation_id in operations:
        if operation_id not in seen_ids:
            seen_ids.add(operation_id)
            import_names.append(operation_id)
        path_entries.append((path_str, operation_id))
    import_line = "from build.views import " + ", ".join(import_names)
    path_lines = [
        f'    path("{path_str}", {op_id}.handler),'
        for path_str, op_id in path_entries
    ]
    urls_content = f'''from django.urls import path
{import_line}

urlpatterns = [
{chr(10).join(path_lines)}
]
'''
    (build_dir / "urls.py").write_text(urls_content, encoding="utf-8")


class Command(BaseCommand):
    help = "Scan api_specs/openapi.yaml in apps, generate build/views and build/urls.py."

    def handle(self, *args, **options):
        build_dir = Path(settings.BASE_DIR) / "build"
        build_views_dir = build_dir / "views"

        if build_dir.exists():
            shutil.rmtree(build_dir)

        build_dir.mkdir(parents=True)
        build_views_dir.mkdir(parents=True)

        (build_dir / "__init__.py").write_text("", encoding="utf-8")
        (build_views_dir / "__init__.py").write_text("", encoding="utf-8")

        operations = list(collect_operations())

        for app_name, path_str, method, operation_id in operations:
            content = f'''from django.views.decorators.csrf import csrf_exempt

from {app_name}.views.{operation_id}.api_wrapper import execute


@csrf_exempt
def handler(request, *args, **kwargs):
    return execute(request)
'''
            write_view_file(build_views_dir, app_name, operation_id, content)

        write_urls(build_dir, operations)

        self.stdout.write(self.style.SUCCESS(f"Build complete: {len(operations)} operation(s)."))
