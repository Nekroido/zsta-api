from dataclasses import dataclass

from pyramid.request import Request

import typing as t


class JsonSerializable:

    def __json__(self, request: Request = None) -> t.Dict:
        """JSON-renderer for this object."""
        from api.utils import serialize
        return serialize(self)


@dataclass
class ApiError(JsonSerializable):
    message: str
    exception: str
    field: str

    def __init__(self, message: str = "", exception: str = "", field: str = ""):
        self.message = message
        self.exception = exception
        self.field = field


class BaseRequest(JsonSerializable):
    pass


class BaseResponse(JsonSerializable):
    pass


@dataclass
class ErrorResponse(BaseResponse):
    errors: t.List[ApiError]

    def __init__(self, errors: t.List[ApiError]):
        self.errors = errors
