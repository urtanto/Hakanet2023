FROM python:3.10-alpine
LABEL authors="vlada"

RUN mkdir proj
WORKDIR proj

ENV PYTHONUNBUFFERED 1

RUN apk update

ADD requirements.txt /proj/
RUN pip install -r requirements.txt

ADD . /proj/
ADD .env.docker /proj/.env

ENTRYPOINT gunicorn Hakanet2023.wsgi:application -b 0.0.0.0:8000
