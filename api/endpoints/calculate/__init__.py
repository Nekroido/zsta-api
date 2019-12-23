from pyramid.config import Configurator


def includeme(config: Configurator) -> None:
    config.add_route('api.calculate', '/api/calculate')
