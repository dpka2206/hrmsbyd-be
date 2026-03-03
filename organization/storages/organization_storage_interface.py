from abc import ABC, abstractmethod


class OrganizationStorageInterface(ABC):
    @abstractmethod
    def create_organization(self, name: str, domain: str, timezone: str):
        pass

    @abstractmethod
    def get_organization_by_id(self, organization_id):
        pass

    @abstractmethod
    def get_organization_by_domain(self, domain: str):
        pass

    @abstractmethod
    def list_organizations(self):
        pass
