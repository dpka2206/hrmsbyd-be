from employees.storages.employee_storage import EmployeeStorage
from workforce.interactors.clock_out_interactor import ClockOutInteractor
from workforce.storages.attendance_storage import AttendanceStorage


def clock_out(input_dto):
    attendance_storage = AttendanceStorage()
    employee_storage = EmployeeStorage()
    interactor = ClockOutInteractor(
        attendance_storage=attendance_storage,
        employee_storage=employee_storage,
    )
    return interactor.execute(input_dto)
