import json

from pyramid.httpexceptions import HTTPException, exception_response, HTTPNotFound
from pyramid.request import Request
from pyramid.view import exception_view_config, notfound_view_config
from pyramid_openapi3 import RequestValidationError

from api.models import ErrorResponse, ApiError
from api.utils import extract_error, serialize


@exception_view_config(RequestValidationError, renderer="json")
def openapi_validation_error(
        context: HTTPException, request: Request
) -> exception_response:
    """If there are errors when handling the request, return them as response."""
    return error(400, ErrorResponse([extract_error(err) for err in context.errors]))


@notfound_view_config(renderer="json")
def notfound(request: Request) -> HTTPNotFound:
    """ Returns formatted 404 error """
    return error(404, ErrorResponse([ApiError("Not found")]))


def error(code: int, error_object: ErrorResponse) -> exception_response:
    """ Transforms ErrorResponse into exception_response with JSON payload """
    body = json.dumps(error_object, default=serialize)
    return exception_response(code, body=body, content_type='application/json', charset='utf-8')
