from organization.exceptions import OrganizationAlreadyExistsException
from organization.interactors.dtos import (
    CreateOrganizationInputDTO,
    CreateOrganizationOutputDTO,
)
from organization.storages.organization_storage_interface import (
    OrganizationStorageInterface,
)


class CreateOrganizationInteractor:
    def __init__(self, organization_storage: OrganizationStorageInterface):
        self._organization_storage = organization_storage

    def execute(self, input_dto: CreateOrganizationInputDTO) -> CreateOrganizationOutputDTO:
        existing = self._organization_storage.get_organization_by_domain(
            input_dto.domain
        )
        if existing is not None:
            raise OrganizationAlreadyExistsException()

        organization = self._organization_storage.create_organization(
            name=input_dto.name,
            domain=input_dto.domain,
            timezone=input_dto.timezone,
        )
        return CreateOrganizationOutputDTO(
            id=organization.id,
            name=organization.name,
            domain=organization.domain,
            timezone=organization.timezone,
            is_active=organization.is_active,
        )
