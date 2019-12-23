from pyramid.config import Configurator


def includeme(config: Configurator) -> None:
    config.include('.calculate')
