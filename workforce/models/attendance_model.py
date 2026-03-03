from django.db import models
from django.db.models import CASCADE

from core.models import BaseModel
from employees.models import EmployeeProfile


class AttendanceDay(BaseModel):
    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Present"
        ABSENT = "ABSENT", "Absent"
        HALF_DAY = "HALF_DAY", "Half Day"

    employee = models.ForeignKey(
        EmployeeProfile,
        on_delete=CASCADE,
        related_name="attendance_days",
    )
    date = models.DateField()
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    total_work_hours = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PRESENT,
    )

    class Meta:
        db_table = "workforce_attendanceday"
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "date"],
                name="workforce_attendanceday_employee_date_uniq",
            )
        ]
        indexes = [
            models.Index(fields=["employee", "date"]),
        ]

    def __str__(self):
        return f"{self.employee.employee_code} - {self.date} ({self.status})"
