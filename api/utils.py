from datetime import date, time

from openapi_core.schema.exceptions import OpenAPIError, OpenAPIMappingError
import typing as t

from setuptools._vendor.packaging import version

from api.models import ApiError


def extract_error(err: OpenAPIError, field_name: str = None) -> ApiError:
    """Extract error JSON response using an Exception instance."""
    error = ApiError(message=str(err), exception=err.__class__.__name__)
    if getattr(err, "name", None) is not None:
        field_name = err.name
    if getattr(err, "property_name", None) is not None:
        field_name = err.property_name
    if field_name is None:
        if isinstance(getattr(err, "original_exception", None), OpenAPIMappingError):
            return extract_error(err.original_exception, field_name)
    if field_name is not None:
        error.field = field_name
    return error


def serialize(obj) -> t.Dict:
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        return obj.isoformat()

    if isinstance(obj, time):
        return obj.isoformat()

    if isinstance(obj, list):
        return [serialize(i) for i in obj]

    return obj.__dict__


class MinVersionPredicate(object):
    def __init__(self, val, config):
        self.min_version = val
        try:
            self.current_version = config.registry.settings['pyramid_openapi3']['spec'].info.version
        except:
            self.current_version = None

    def text(self):
        return 'min_version = %s' % (self.min_version,)

    phash = text

    def __call__(self, context, request):
        selected_version = request.headers.get('X-API-VERSION', self.current_version)
        return selected_version is not None and version.parse(selected_version).__le__(version.parse(self.min_version))
