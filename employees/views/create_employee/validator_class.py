import uuid
from datetime import datetime


class CreateEmployeeValidator:
    REQUIRED = (
        "user_id",
        "organization_id",
        "employee_code",
        "employment_type",
        "joining_date",
    )
    EMPLOYMENT_TYPES = ("FULL_TIME", "PART_TIME", "INTERN")
    DATE_FORMAT = "%Y-%m-%d"
    UUID_FIELDS = ("user_id", "organization_id")
    OPTIONAL_UUID_FIELDS = ("department_id", "designation_id")

    def __init__(self, data: dict):
        self._data = data

    def validate(self) -> dict:
        data = self._data
        if data is None or (isinstance(data, dict) and len(data) == 0):
            raise ValueError("Request body is required.")
        if not isinstance(data, dict):
            raise ValueError("Request body must be a JSON object.")

        missing = [k for k in self.REQUIRED if data.get(k) is None or data.get(k) == ""]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}.")

        cleaned = {}

        for field in self.UUID_FIELDS:
            value = data[field]
            cleaned[field] = self._validate_uuid(value, field)

        for field in self.OPTIONAL_UUID_FIELDS:
            value = data.get(field)
            if value is None or value == "":
                cleaned[field] = None
            else:
                cleaned[field] = self._validate_uuid(value, field)

        employee_code = data["employee_code"]
        if not isinstance(employee_code, str):
            raise ValueError("employee_code must be a string.")
        cleaned["employee_code"] = employee_code.strip()
        if not cleaned["employee_code"]:
            raise ValueError("employee_code cannot be empty.")

        employment_type = data["employment_type"]
        if not isinstance(employment_type, str):
            raise ValueError("employment_type must be a string.")
        employment_type = employment_type.strip().upper()
        if employment_type not in self.EMPLOYMENT_TYPES:
            raise ValueError(
                f"employment_type must be one of: {', '.join(self.EMPLOYMENT_TYPES)}."
            )
        cleaned["employment_type"] = employment_type

        joining_date_raw = data["joining_date"]
        cleaned["joining_date"] = self._validate_date(joining_date_raw)

        return cleaned

    def _validate_uuid(self, value, field_name: str) -> str:
        if value is None:
            raise ValueError(f"{field_name} is required.")
        s = str(value).strip()
        try:
            uuid.UUID(s)
        except (ValueError, TypeError):
            raise ValueError(f"{field_name} must be a valid UUID.") from None
        return s

    def _validate_date(self, value) -> str:
        if value is None or value == "":
            raise ValueError("joining_date is required.")
        s = str(value).strip()
        try:
            datetime.strptime(s, self.DATE_FORMAT)
        except ValueError:
            raise ValueError(
                f"joining_date must be a date in YYYY-MM-DD format."
            ) from None
        return s
