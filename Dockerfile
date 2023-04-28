FROM python:3.10
LABEL authors="vlada"

RUN mkdir proj
WORKDIR proj

ENV PYTHONUNBUFFERED 1

ADD . /proj/
ADD .env.docker /proj/.env

RUN pip install -r requipments.txt

CMD gunicorn Hakanet2023.wsgi:application -b 0.0.0.0:8000
