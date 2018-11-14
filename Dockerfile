FROM python:3.6-alpine

LABEL maintainer="HayatoDoi"

WORKDIR /scripts
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY *.py ./
