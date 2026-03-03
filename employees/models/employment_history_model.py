from django.db import models
from django.db.models import CASCADE, SET_NULL

from core.models import BaseModel
from organization.models import Department, Designation

from .employees_model import EmployeeProfile


class EmploymentHistory(BaseModel):
    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=CASCADE,
        related_name="employment_histories",
    )
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=SET_NULL,
        related_name="employment_histories",
    )
    designation = models.ForeignKey(
        Designation,
        null=True,
        on_delete=SET_NULL,
        related_name="employment_histories",
    )
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "employees_employmenthistory"
        ordering = ["-effective_from"]
        indexes = [
            models.Index(fields=["employee", "effective_from"]),
        ]
