import os

from pyramid.config import Configurator
from pyramid.renderers import JSON

from api.utils import MinVersionPredicate


def includeme(config: Configurator) -> None:
    config.include("pyramid_openapi3")
    config.pyramid_openapi3_spec(
        os.path.join(os.path.dirname(__file__), "openapi.yaml"), route='/openapi.yaml'
    )
    config.pyramid_openapi3_add_explorer(route='/api')
    config.add_renderer("json", json_renderer())
    config.add_view_predicate('min_version', MinVersionPredicate)


def json_renderer() -> JSON:
    """Configure a JSON renderer that supports rendering datetimes."""
    renderer = JSON()
    return renderer
