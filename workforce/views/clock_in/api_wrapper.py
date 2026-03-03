import json

from rest_framework.response import Response

from workforce.exceptions.exceptions import (
    AlreadyClockedInException,
    EmployeeNotActiveException,
)
from workforce.presenters.attendance_presenter import AttendancePresenter
from workforce.views.clock_in.clock_in import clock_in
from workforce.views.clock_in.validator_class import ClockInValidator


def execute(request):
    if hasattr(request, "data"):
        data = request.data
    else:
        data = json.loads(request.body.decode("utf-8")) if request.body else {}

    presenter = AttendancePresenter()
    validator = ClockInValidator(data)
    try:
        input_dto = validator.validate()
    except ValueError as e:
        return Response(presenter.present_error(str(e)), status=400)

    try:
        output_dto = clock_in(input_dto)
        return Response(presenter.present_clock_in_success(output_dto), status=200)
    except EmployeeNotActiveException:
        return Response(
            presenter.present_error("Employee not found or not active."),
            status=404,
        )
    except AlreadyClockedInException:
        return Response(
            presenter.present_error("Already clocked in for today."),
            status=409,
        )
