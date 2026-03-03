from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateEmployeeInputDTO:
    user_id: str
    organization_id: str
    employee_code: str
    employment_type: str
    joining_date: str  # date as string (e.g. ISO) or use date type
    department_id: Optional[str] = None
    designation_id: Optional[str] = None


@dataclass
class CreateEmployeeOutputDTO:
    id: str
    employee_code: str
    organization_id: str
    status: str
