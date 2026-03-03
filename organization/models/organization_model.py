from core.models import BaseModel
from django.db import models


class Organization(BaseModel):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True, db_index=True)
    timezone = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "organization_organization"

    def __str__(self):
        return self.name


class Department(BaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="departments"
    )
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        db_table = "organization_department"
        unique_together = [["organization", "name"]]

    def __str__(self):
        return self.name


class Designation(BaseModel):
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="designations"
    )
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        db_table = "organization_designation"
        unique_together = [["organization", "name"]]

    def __str__(self):
        return self.name
