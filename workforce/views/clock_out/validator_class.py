import uuid

from workforce.interactors.dtos import ClockOutInputDTO


class ClockOutValidator:
    def __init__(self, data: dict):
        self._data = data

    def validate(self) -> ClockOutInputDTO:
        if self._data is None or (isinstance(self._data, dict) and len(self._data) == 0):
            raise ValueError("Request body is required.")
        if not isinstance(self._data, dict):
            raise ValueError("Request body must be a JSON object.")
        data = self._data
        employee_id = data.get("employee_id")
        if employee_id is None or employee_id == "":
            raise ValueError("employee_id is required.")
        s = str(employee_id).strip()
        try:
            uuid.UUID(s)
        except (ValueError, TypeError):
            raise ValueError("employee_id must be a valid UUID.") from None
        return ClockOutInputDTO(employee_id=s)
