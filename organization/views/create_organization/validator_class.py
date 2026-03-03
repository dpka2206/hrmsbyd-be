from organization.interactors.dtos import CreateOrganizationInputDTO


class CreateOrganizationValidator:
    REQUIRED = ("name", "domain", "timezone")

    def validate(self, data: dict) -> CreateOrganizationInputDTO:
        missing = [k for k in self.REQUIRED if not data.get(k)]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
        return CreateOrganizationInputDTO(
            name=str(data["name"]).strip(),
            domain=str(data["domain"]).strip(),
            timezone=str(data["timezone"]).strip(),
        )
