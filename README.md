# Sample API
Proof of concept extendable API based on Pyramid framework for Python.

## Usage

This section covers project startup, creating/updating endpoints and running tests.

### Starting up
With bash:
```shell script
cd <directory containing this file>
pip install --upgrade pip
pip install -e .
python3 setup.py develop
pserve development.ini --reload
```

With docker-compose
```shell script
docker-compose up  --build
```

### Adding new endpoints
Create new python package in `api/endpoints` folder and define its routes:
```python
def includeme(config: Configurator) -> None:
    config.add_route('api.new_endpoint', '/api/new_endpoint')
``` 

Create and define the endpoint's views in `versions.py`. You can create new version of a view by adding `min_version` property for `view_config()` decorator.
```python
@view_config(route_name='api.new_endpoint', renderer="json", request_method="GET", openapi=True,
             min_version="0.0.0")
def custom_endpoint(request: Request) -> BaseResponse:
    ...

@view_config(route_name='api.new_endpoint', renderer="json", request_method="GET", openapi=True,
             min_version="0.0.1")
def new_custom_endpoint(request: Request) -> BaseResponse:
    ...
```
Don't forget to cover your endpoint with tests! Finally, describe the new endpoint and its schema in `api/openapi.yaml`.

---
Refer to `api/endpoints/calculate` for examples.

### Tests
Run the following command to execute project's tests.
```shell script
python3 setup.py test
```

## Volumes
* /usr/src/app/api

## Ports
* 6543

## Contributing
Pull requests and suggestions are welcome!

## Authors
* [Nekroido](https://github.com/nekroido)

## Licence
[MIT](LICENSE)
