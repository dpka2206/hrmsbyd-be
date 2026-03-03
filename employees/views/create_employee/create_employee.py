from accounts.storages import UserStorage
from employees.interactors.create_employee_interactor import CreateEmployeeInteractor
from employees.interactors.dtos import CreateEmployeeInputDTO, CreateEmployeeOutputDTO
from employees.presenters.employee_presenter import EmployeePresenter
from employees.storages.employee_storage import EmployeeStorage
from organization.storages import OrganizationStorage


def create_employee(input_dto: CreateEmployeeInputDTO) -> dict:
    employee_storage = EmployeeStorage()
    organization_storage = OrganizationStorage()
    user_storage = UserStorage()
    presenter = EmployeePresenter()
    interactor = CreateEmployeeInteractor(
        employee_storage=employee_storage,
        organization_storage=organization_storage,
        user_storage=user_storage,
    )
    output_dto: CreateEmployeeOutputDTO = interactor.execute(input_dto)
    return presenter.present_success(output_dto)
