from employees.models import EmployeeProfile

from workforce.models import AttendanceDay
from workforce.storages.attendance_storage_interface import AttendanceStorageInterface


class AttendanceStorage(AttendanceStorageInterface):
    def get_attendance_for_day(self, employee_id, date):
        try:
            return AttendanceDay.objects.get(employee_id=employee_id, date=date)
        except AttendanceDay.DoesNotExist:
            return None

    def create_attendance(self, employee_id, date, clock_in_time):
        try:
            employee = EmployeeProfile.objects.get(pk=employee_id)
        except EmployeeProfile.DoesNotExist:
            return None
        return AttendanceDay.objects.create(
            employee=employee,
            date=date,
            clock_in_time=clock_in_time,
        )

    def update_clock_out(self, attendance_id, clock_out_time, total_work_hours):
        try:
            attendance = AttendanceDay.objects.get(pk=attendance_id)
        except AttendanceDay.DoesNotExist:
            return None
        attendance.clock_out_time = clock_out_time
        attendance.total_work_hours = total_work_hours
        attendance.save()
        return attendance
