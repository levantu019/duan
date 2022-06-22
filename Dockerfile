FROM python:3.9.13-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /duan_be
WORKDIR /duan_be

COPY requirements.txt /duan_be/
RUN pip install -r requirements.txt 

COPY ./duan /duan_be