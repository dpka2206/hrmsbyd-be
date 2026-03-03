from organization.interactors.dtos import CreateOrganizationOutputDTO


class OrganizationPresenter:
    def present_success(self, output_dto: CreateOrganizationOutputDTO) -> dict:
        return {
            "id": str(output_dto.id),
            "name": output_dto.name,
            "domain": output_dto.domain,
            "timezone": output_dto.timezone,
            "is_active": output_dto.is_active,
        }

    def present_error(self, message: str) -> dict:
        return {
            "error": message,
        }
