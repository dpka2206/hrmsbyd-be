class EmployeeNotActiveException(Exception):
    """Raised when the employee is not active (e.g. inactive or terminated)."""

    pass


class AlreadyClockedInException(Exception):
    """Raised when the employee has already clocked in for the day."""

    pass


class NotClockedInException(Exception):
    """Raised when the employee has not clocked in (e.g. cannot clock out)."""

    pass
