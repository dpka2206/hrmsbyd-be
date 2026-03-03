from django.contrib.auth import get_user_model

from employees.models import EmployeeProfile
from employees.storages.employee_storage_interface import EmployeeStorageInterface
from organization.models import Department, Designation, Organization


class EmployeeStorage(EmployeeStorageInterface):
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
        User = get_user_model()
        user = User.objects.get(pk=user_id)
        organization = Organization.objects.get(pk=organization_id)
        department = None
        if department_id is not None:
            department = Department.objects.get(pk=department_id)
        designation = None
        if designation_id is not None:
            designation = Designation.objects.get(pk=designation_id)
        return EmployeeProfile.objects.create(
            user=user,
            organization=organization,
            employee_code=employee_code,
            department=department,
            designation=designation,
            employment_type=employment_type,
            joining_date=joining_date,
        )

    def get_employee_by_id(self, employee_id):
        try:
            return EmployeeProfile.objects.get(pk=employee_id)
        except EmployeeProfile.DoesNotExist:
            return None

    def get_employee_by_user_id(self, user_id):
        try:
            return EmployeeProfile.objects.get(user_id=user_id)
        except EmployeeProfile.DoesNotExist:
            return None

    def check_employee_code_exists(self, employee_code, organization_id):
        return EmployeeProfile.objects.filter(
            employee_code=employee_code,
            organization_id=organization_id,
        ).exists()
