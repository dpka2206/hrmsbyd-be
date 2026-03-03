from dataclasses import dataclass


@dataclass
class ClockInInputDTO:
    employee_id: str


@dataclass
class ClockOutInputDTO:
    employee_id: str


@dataclass
class ClockInOutputDTO:
    attendance_id: str
    clock_in_time: str
    date: str


@dataclass
class ClockOutOutputDTO:
    attendance_id: str
    clock_out_time: str
    total_work_hours: float
