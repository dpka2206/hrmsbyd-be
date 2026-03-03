from django.contrib import admin

from .models import AttendanceDay


@admin.register(AttendanceDay)
class AttendanceDayAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "status", "clock_in_time", "clock_out_time", "total_work_hours")
    list_filter = ("status", "date")
    search_fields = ("employee__employee_code",)
