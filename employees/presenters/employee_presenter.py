from employees.interactors.dtos import CreateEmployeeOutputDTO


class EmployeePresenter:
    def present_success(self, output_dto: CreateEmployeeOutputDTO) -> dict:
        return {
            "success": True,
            "data": {
                "id": output_dto.id,
                "employee_code": output_dto.employee_code,
                "organization_id": output_dto.organization_id,
                "status": output_dto.status,
            },
        }

    def present_error(self, message: str) -> dict:
        return {
            "success": False,
            "error": message,
        }
