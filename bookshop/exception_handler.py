import json
from http import HTTPStatus

from rest_framework.views import exception_handler
from rest_framework.response import Response

from bookshop.errors import RecordNotFound, ValidationError


def bookshop_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        response = ExceptionHandler.handle(exc, context)

    return response


class ExceptionHandler:
    @classmethod
    def handle(cls, exc, context):
        exc_type = type(exc)
        if exc_type == RecordNotFound:
            status = HTTPStatus.NOT_FOUND
        elif exc_type == ValidationError:
            status = HTTPStatus.UNPROCESSABLE_CONTENT
        else:
            status = HTTPStatus.INTERNAL_SERVER_ERROR

        r = cls._create_response(exc, status)
        return r

    @staticmethod
    def _create_response(exc, status: int) -> Response:
        if status == HTTPStatus.INTERNAL_SERVER_ERROR:
            data = str(exc)
        else:
            data = {"error": {"message": exc.msg, "type": exc.error_type}}

        response = Response(data=json.dumps(data), status=status, content_type="json")
        return response
