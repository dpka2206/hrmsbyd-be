from datetime import date, datetime

from employees.storages.employee_storage_interface import EmployeeStorageInterface
from workforce.exceptions.exceptions import (
    AlreadyClockedInException,
    EmployeeNotActiveException,
    NotClockedInException,
)
from workforce.interactors.dtos import ClockOutInputDTO, ClockOutOutputDTO
from workforce.storages.attendance_storage_interface import AttendanceStorageInterface


class ClockOutInteractor:
    def __init__(
        self,
        *,
        attendance_storage: AttendanceStorageInterface,
        employee_storage: EmployeeStorageInterface,
    ):
        self._attendance_storage = attendance_storage
        self._employee_storage = employee_storage

    def execute(self, input_dto: ClockOutInputDTO) -> ClockOutOutputDTO:
        employee = self._employee_storage.get_employee_by_id(input_dto.employee_id)
        if employee is None:
            raise EmployeeNotActiveException()
        if employee.status != "ACTIVE":
            raise EmployeeNotActiveException()

        today = date.today()
        attendance = self._attendance_storage.get_attendance_for_day(
            input_dto.employee_id,
            today,
        )
        if attendance is None or attendance.clock_in_time is None:
            raise NotClockedInException()
        if attendance.clock_out_time is not None:
            raise AlreadyClockedInException()

        now = datetime.now()
        total_work_hours = (now - attendance.clock_in_time).total_seconds() / 3600

        updated = self._attendance_storage.update_clock_out(
            attendance_id=attendance.id,
            clock_out_time=now,
            total_work_hours=total_work_hours,
        )
        if updated is None:
            raise NotClockedInException()

        return ClockOutOutputDTO(
            attendance_id=str(updated.id),
            clock_out_time=updated.clock_out_time.isoformat() if updated.clock_out_time else "",
            total_work_hours=updated.total_work_hours or 0.0,
        )
