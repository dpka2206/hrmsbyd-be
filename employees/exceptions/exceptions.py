class OrganizationNotFoundException(Exception):
    """Raised when an organization is not found."""

    pass


class EmployeeAlreadyExistsException(Exception):
    """Raised when an employee already exists (e.g. duplicate employee code or user)."""

    pass


class UserNotFoundException(Exception):
    """Raised when a user is not found."""

    pass
