from django.conf import settings
from django.db import models
from django.db.models import CASCADE, SET_NULL

from core.models import BaseModel
from organization.models import Department, Designation, Organization


class EmployeeProfile(BaseModel):
    class EmploymentType(models.TextChoices):
        FULL_TIME = "FULL_TIME", "Full Time"
        PART_TIME = "PART_TIME", "Part Time"
        INTERN = "INTERN", "Intern"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        TERMINATED = "TERMINATED", "Terminated"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name="employee_profile",
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=CASCADE,
        related_name="employee_profiles",
    )
    employee_code = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="employee_profiles",
    )
    designation = models.ForeignKey(
        Designation,
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="employee_profiles",
    )
    reporting_manager = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=SET_NULL,
        related_name="reportees",
    )
    employment_type = models.CharField(
        max_length=20,
        choices=EmploymentType.choices,
    )
    joining_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    class Meta:
        db_table = "employees_employeeprofile"
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["employee_code", "organization"],
                name="employees_employeeprofile_employee_code_organization_uniq",
            )
        ]

    def __str__(self):
        return f"{self.employee_code} - {self.user.get_full_name() or self.user.username}"
