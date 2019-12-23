from dataclasses import dataclass

from api.models import BaseResponse, BaseRequest


@dataclass
class CalculateRequest(BaseRequest):
    expression: str


@dataclass
class CalculateResponse(BaseResponse):
    result: float
