from abc import ABC, abstractmethod


class AttendanceStorageInterface(ABC):
    @abstractmethod
    def get_attendance_for_day(self, employee_id, date):
        pass

    @abstractmethod
    def create_attendance(self, employee_id, date, clock_in_time):
        pass

    @abstractmethod
    def update_clock_out(self, attendance_id, clock_out_time, total_work_hours):
        pass
