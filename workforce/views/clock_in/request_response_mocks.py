CLOCK_IN_REQUEST_MOCK = {
    "employee_id": "00000000-0000-0000-0000-000000000001",
}

CLOCK_IN_RESPONSE_200_MOCK = {
    "success": True,
    "data": {
        "attendance_id": "00000000-0000-0000-0000-000000000002",
        "clock_in_time": "2025-03-03T10:00:00",
        "date": "2025-03-03",
    },
}

CLOCK_IN_RESPONSE_404_MOCK = {"success": False, "error": "Employee not found or not active."}

CLOCK_IN_RESPONSE_409_MOCK = {"success": False, "error": "Already clocked in for today."}
