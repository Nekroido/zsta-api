from pyramid.request import Request
from pyramid.view import view_config
from calculator.simple import SimpleCalculator

from api.endpoints.calculate.models import CalculateResponse


@view_config(route_name='api.calculate', renderer="json", request_method="POST", openapi=True,
             min_version="0.0.0")
def calculate_v1(request: Request) -> CalculateResponse:
    expression = request.openapi_validated.body.expression
    calc = SimpleCalculator()
    calc.run(expression)
    return CalculateResponse(result=calc.lcd)


@view_config(route_name='api.calculate', renderer="json", request_method="POST", openapi=True,
             min_version="0.0.1")
def calculate_v2(request: Request) -> CalculateResponse:
    print('I now also spam into stdout!')
    return calculate_v1(request)
