FROM python:3.8

WORKDIR /firsttest

COPY . $WORKDIR

RUN pip install -r requirements.txt