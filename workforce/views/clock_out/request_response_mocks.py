CLOCK_OUT_REQUEST_MOCK = {
    "employee_id": "00000000-0000-0000-0000-000000000001",
}

CLOCK_OUT_RESPONSE_200_MOCK = {
    "success": True,
    "data": {
        "attendance_id": "00000000-0000-0000-0000-000000000002",
        "clock_out_time": "2025-03-03T18:00:00",
        "total_work_hours": 8.0,
    },
}

CLOCK_OUT_RESPONSE_404_MOCK = {"success": False, "error": "Not clocked in. Cannot clock out."}

CLOCK_OUT_RESPONSE_409_MOCK = {"success": False, "error": "Already clocked out for today."}
