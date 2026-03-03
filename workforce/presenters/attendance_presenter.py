from workforce.interactors.dtos import ClockInOutputDTO, ClockOutOutputDTO


class AttendancePresenter:
    def present_clock_in_success(self, output_dto: ClockInOutputDTO) -> dict:
        return {
            "success": True,
            "data": {
                "attendance_id": output_dto.attendance_id,
                "clock_in_time": output_dto.clock_in_time,
                "date": output_dto.date,
            },
        }

    def present_clock_out_success(self, output_dto: ClockOutOutputDTO) -> dict:
        return {
            "success": True,
            "data": {
                "attendance_id": output_dto.attendance_id,
                "clock_out_time": output_dto.clock_out_time,
                "total_work_hours": output_dto.total_work_hours,
            },
        }

    def present_error(self, message: str) -> dict:
        return {
            "success": False,
            "error": message,
        }
