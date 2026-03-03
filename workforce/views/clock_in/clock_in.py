from employees.storages.employee_storage import EmployeeStorage
from workforce.interactors.clock_in_interactor import ClockInInteractor
from workforce.storages.attendance_storage import AttendanceStorage


def clock_in(input_dto):
    attendance_storage = AttendanceStorage()
    employee_storage = EmployeeStorage()
    interactor = ClockInInteractor(
        attendance_storage=attendance_storage,
        employee_storage=employee_storage,
    )
    return interactor.execute(input_dto)
