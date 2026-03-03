import logging

from accounts.storages.user_storage_interface import UserStorageInterface
from employees.exceptions.exceptions import (
    EmployeeAlreadyExistsException,
    OrganizationNotFoundException,
    UserNotFoundException,
)
from employees.interactors.dtos import CreateEmployeeInputDTO, CreateEmployeeOutputDTO
from employees.storages.employee_storage_interface import EmployeeStorageInterface
from organization.storages.organization_storage_interface import (
    OrganizationStorageInterface,
)

logger = logging.getLogger(__name__)


class CreateEmployeeInteractor:
    def __init__(
        self,
        *,
        employee_storage: EmployeeStorageInterface,
        organization_storage: OrganizationStorageInterface,
        user_storage: UserStorageInterface,
    ):
        self._employee_storage = employee_storage
        self._organization_storage = organization_storage
        self._user_storage = user_storage

    def execute(self, input_dto: CreateEmployeeInputDTO) -> CreateEmployeeOutputDTO:
        logger.info(
            "Employee creation started",
            extra={
                "organization_id": input_dto.organization_id,
                "employee_code": input_dto.employee_code,
            },
        )
        organization = self._organization_storage.get_organization_by_id(
            input_dto.organization_id
        )
        if organization is None:
            raise OrganizationNotFoundException()

        user = self._user_storage.get_user_by_id(input_dto.user_id)
        if user is None:
            raise UserNotFoundException()

        if self._employee_storage.check_employee_code_exists(
            input_dto.employee_code,
            input_dto.organization_id,
        ):
            logger.warning(
                "Duplicate employee code detected for organization",
                extra={
                    "organization_id": input_dto.organization_id,
                    "employee_code": input_dto.employee_code,
                },
            )
            raise EmployeeAlreadyExistsException()

        employee = self._employee_storage.create_employee(
            user_id=input_dto.user_id,
            organization_id=input_dto.organization_id,
            employee_code=input_dto.employee_code,
            department_id=input_dto.department_id,
            designation_id=input_dto.designation_id,
            employment_type=input_dto.employment_type,
            joining_date=input_dto.joining_date,
        )

        output_dto = CreateEmployeeOutputDTO(
            id=str(employee.id),
            employee_code=employee.employee_code,
            organization_id=str(employee.organization_id),
            status=employee.status,
        )
        logger.info(
            "Employee creation successful",
            extra={
                "employee_id": str(employee.id),
                "employee_code": employee.employee_code,
                "organization_id": str(employee.organization_id),
            },
        )
        return output_dto
