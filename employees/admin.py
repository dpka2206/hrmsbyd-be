from django.contrib import admin

from .models import EmployeeProfile


@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "user", "organization", "status")
    list_filter = ("status", "organization")
    search_fields = ("employee_code", "user__email")
