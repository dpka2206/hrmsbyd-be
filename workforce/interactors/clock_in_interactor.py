from datetime import date, datetime

from employees.storages.employee_storage_interface import EmployeeStorageInterface
from workforce.exceptions.exceptions import (
    AlreadyClockedInException,
    EmployeeNotActiveException,
)
from workforce.interactors.dtos import ClockInInputDTO, ClockInOutputDTO
from workforce.storages.attendance_storage_interface import AttendanceStorageInterface


class ClockInInteractor:
    def __init__(
        self,
        *,
        attendance_storage: AttendanceStorageInterface,
        employee_storage: EmployeeStorageInterface,
    ):
        self._attendance_storage = attendance_storage
        self._employee_storage = employee_storage

    def execute(self, input_dto: ClockInInputDTO) -> ClockInOutputDTO:
        employee = self._employee_storage.get_employee_by_id(input_dto.employee_id)
        if employee is None:
            raise EmployeeNotActiveException()
        if employee.status != "ACTIVE":
            raise EmployeeNotActiveException()

        today = date.today()
        existing = self._attendance_storage.get_attendance_for_day(
            input_dto.employee_id,
            today,
        )
        if existing is not None:
            raise AlreadyClockedInException()

        attendance = self._attendance_storage.create_attendance(
            employee_id=input_dto.employee_id,
            date=today,
            clock_in_time=datetime.now(),
        )
        if attendance is None:
            raise EmployeeNotActiveException()

        return ClockInOutputDTO(
            attendance_id=str(attendance.id),
            clock_in_time=attendance.clock_in_time.isoformat() if attendance.clock_in_time else "",
            date=attendance.date.isoformat(),
        )
</think>
Simplifying logic: if any attendance record exists for today, raise AlreadyClockedInException; otherwise create.
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
StrReplace