FROM python:3.7-slim

RUN mkdir /app
WORKDIR /app

COPY . .

RUN python setup.py install