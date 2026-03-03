import json

from rest_framework.response import Response

from organization.views.create_organization.create_organization import (
    create_organization,
)
from organization.views.create_organization.validator_class import (
    CreateOrganizationValidator,
)


def execute(request):
    if hasattr(request, "data"):
        data = request.data
    else:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}

    validator = CreateOrganizationValidator()
    try:
        input_dto = validator.validate(data)
    except ValueError as e:
        return Response({"error": str(e)}, status=400)

    response_data, status_code = create_organization(input_dto)
    return Response(response_data, status=status_code)
