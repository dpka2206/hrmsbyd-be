import json

from rest_framework.response import Response

from employees.exceptions.exceptions import (
    EmployeeAlreadyExistsException,
    OrganizationNotFoundException,
    UserNotFoundException,
)
from employees.interactors.dtos import CreateEmployeeInputDTO
from employees.presenters.employee_presenter import EmployeePresenter
from employees.views.create_employee.create_employee import create_employee
from employees.views.create_employee.validator_class import CreateEmployeeValidator


def execute(request):
    if hasattr(request, "data"):
        data = request.data
    else:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}

    presenter = EmployeePresenter()
    validator = CreateEmployeeValidator(data)
    try:
        cleaned = validator.validate()
    except ValueError as e:
        return Response(presenter.present_error(str(e)), status=400)

    input_dto = CreateEmployeeInputDTO(
        user_id=cleaned["user_id"],
        organization_id=cleaned["organization_id"],
        employee_code=cleaned["employee_code"],
        employment_type=cleaned["employment_type"],
        joining_date=cleaned["joining_date"],
        department_id=cleaned.get("department_id"),
        designation_id=cleaned.get("designation_id"),
    )

    try:
        response_data = create_employee(input_dto)
        return Response(response_data, status=201)
    except OrganizationNotFoundException:
        return Response(
            presenter.present_error("Organization not found."),
            status=404,
        )
    except UserNotFoundException:
        return Response(
            presenter.present_error("User not found."),
            status=404,
        )
    except EmployeeAlreadyExistsException:
        return Response(
            presenter.present_error(
                "Employee with this code already exists in organization."
            ),
            status=409,
        )
