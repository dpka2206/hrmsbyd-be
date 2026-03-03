from organization.models import Organization
from organization.storages.organization_storage_interface import (
    OrganizationStorageInterface,
)


class OrganizationStorage(OrganizationStorageInterface):
    def create_organization(self, name: str, domain: str, timezone: str):
        return Organization.objects.create(
            name=name,
            domain=domain,
            timezone=timezone,
        )

    def get_organization_by_id(self, organization_id):
        try:
            return Organization.objects.get(pk=organization_id)
        except Organization.DoesNotExist:
            return None

    def get_organization_by_domain(self, domain: str):
        try:
            return Organization.objects.get(domain=domain)
        except Organization.DoesNotExist:
            return None

    def list_organizations(self):
        return Organization.objects.all()
