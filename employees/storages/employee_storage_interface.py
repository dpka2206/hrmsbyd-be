from abc import ABC, abstractmethod


class EmployeeStorageInterface(ABC):
    @abstractmethod
    def create_employee(
        self,
        user_id,
        organization_id,
        employee_code,
        department_id,
        designation_id,
        employment_type,
        joining_date,
    ):
        pass

    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_employee_by_user_id(self, user_id):
        pass

    @abstractmethod
    def check_employee_code_exists(self, employee_code, organization_id):
        pass
