CREATE_EMPLOYEE_REQUEST_MOCK = {
    "user_id": "00000000-0000-0000-0000-000000000001",
    "organization_id": "00000000-0000-0000-0000-000000000002",
    "employee_code": "EMP001",
    "employment_type": "FULL_TIME",
    "joining_date": "2025-01-15",
    "department_id": None,
    "designation_id": None,
}

CREATE_EMPLOYEE_RESPONSE_201_MOCK = {
    "id": "00000000-0000-0000-0000-000000000003",
    "employee_code": "EMP001",
    "organization_id": "00000000-0000-0000-0000-000000000002",
    "status": "ACTIVE",
}

CREATE_EMPLOYEE_RESPONSE_404_MOCK = {"error": "Organization not found."}

CREATE_EMPLOYEE_RESPONSE_409_MOCK = {
    "error": "Employee with this code already exists in organization."
}
