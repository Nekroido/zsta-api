FROM python:3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y --no-install-recommends

COPY . .

RUN pip install --upgrade pip
RUN pip install -e .
RUN python3 setup.py develop

CMD [ "pserve", "development.ini", "--reload" ]
