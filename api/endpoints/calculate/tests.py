from openapi_core.validation.request.models import RequestValidationResult
from pyramid import testing
from pyramid.testing import DummyRequest

from api.tests import BaseFunctionalTests, BaseViewTests
from api.utils import serialize
from .models import CalculateRequest
from .versions import *

# TODO: Create fixtures
valid_expression = '3 + 2'
valid_result = 5
invalid_result = 21


class ViewTests(BaseViewTests):

    @property
    def empty_request(self) -> DummyRequest:
        return testing.DummyRequest()

    @property
    def valid_request(self) -> DummyRequest:
        request = testing.DummyRequest()
        request.openapi_validated = RequestValidationResult([], CalculateRequest(expression=valid_expression))
        return request

    @property
    def valid_response(self) -> CalculateResponse:
        return CalculateResponse(result=valid_result)

    @property
    def invalid_response(self) -> CalculateResponse:
        return CalculateResponse(result=invalid_result)

    def test_calculate_v2(self):
        self.test_calculate_v1(calculate_v2)

    def test_calculate_v1(self, predicate=calculate_v1):
        self.assertEqual(predicate(self.valid_request), self.valid_response)
        self.assertNotEqual(predicate(self.valid_request), self.invalid_response)
        with self.assertRaises(AttributeError):
            predicate(self.empty_request)


class FunctionalTests(BaseFunctionalTests):
    endpoint = '/api/calculate'

    def create_request_object(self, expression):
        return serialize(CalculateRequest(expression=expression))

    @property
    def valid_request(self):
        return self.create_request_object(valid_expression)

    def test_endpoint(self):
        # Test invalid request method
        get = self.testapp.get(self.endpoint, status=404, expect_errors=True)
        self.assertEqual(get.status_code, 404)

        # Test empty payload
        post = self.testapp.post(self.endpoint, expect_errors=True)
        self.assertEqual(post.status_code, 400)

        # Test valid payload
        post = self.testapp.post_json(
            self.endpoint,
            params=self.valid_request,
            content_type='application/json',
            expect_errors=True
        )
        self.assertEqual(post.status_code, 200)
        self.assertIsNotNone(post.json)
        self.assertEqual(post.json.get('result', None), valid_result)
