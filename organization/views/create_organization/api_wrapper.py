import json

from django.http import JsonResponse

from organization.exceptions import OrganizationAlreadyExistsException
from organization.interactors.dtos import CreateOrganizationInputDTO
from organization.interactors.create_organization_interactor import (
    CreateOrganizationInteractor,
)
from organization.presenters import OrganizationPresenter
from organization.storages import OrganizationStorage


def execute(request):
    if hasattr(request, "data"):
        data = request.data
    else:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}
    input_dto = CreateOrganizationInputDTO(
        name=data["name"],
        domain=data["domain"],
        timezone=data["timezone"],
    )
    storage = OrganizationStorage()
    presenter = OrganizationPresenter()
    interactor = CreateOrganizationInteractor(organization_storage=storage)
    try:
        output_dto = interactor.execute(input_dto)
        return JsonResponse(
            presenter.present_success(output_dto),
            status=201,
        )
    except OrganizationAlreadyExistsException:
        return JsonResponse(
            presenter.present_error("Organization with this domain already exists."),
            status=409,
        )
