from organization.exceptions import OrganizationAlreadyExistsException
from organization.interactors.create_organization_interactor import (
    CreateOrganizationInteractor,
)
from organization.interactors.dtos import (
    CreateOrganizationInputDTO,
    CreateOrganizationOutputDTO,
)
from organization.presenters import OrganizationPresenter
from organization.storages import OrganizationStorage


def create_organization(input_dto: CreateOrganizationInputDTO) -> tuple[dict, int]:
    storage = OrganizationStorage()
    presenter = OrganizationPresenter()
    interactor = CreateOrganizationInteractor(organization_storage=storage)

    try:
        output_dto: CreateOrganizationOutputDTO = interactor.execute(input_dto)
        return (presenter.present_success(output_dto), 201)
    except OrganizationAlreadyExistsException:
        return (
            presenter.present_error(
                "Organization with this domain already exists."
            ),
            409,
        )
