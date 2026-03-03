import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class CreateOrganizationInputDTO:
    name: str
    domain: str
    timezone: str


@dataclass(frozen=True)
class CreateOrganizationOutputDTO:
    id: uuid.UUID
    name: str
    domain: str
    timezone: str
    is_active: bool
