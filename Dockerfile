FROM python:3.10-alpine
LABEL authors="urtanto"

RUN mkdir proj
WORKDIR /proj

ENV PYTHONUNBUFFERED 1
ENV Server_starts "true"

RUN apk update

ADD requirements.txt /proj/
RUN pip install -r requirements.txt

ADD . /proj/
ADD .env.docker /proj/.env

ENTRYPOINT gunicorn Hakanet2023.wsgi:application -b 0.0.0.0:8000
