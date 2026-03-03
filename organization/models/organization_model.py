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
