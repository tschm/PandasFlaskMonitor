# Set the base image to Ubuntu
FROM continuumio/miniconda3

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

RUN conda install -q -y pandas=0.18.1 flask=0.10.1

RUN pip install gunicorn gevent

ADD . /pymonitor

WORKDIR /pymonitor

ENV WEBSERVER_SETTINGS /pymonitor/config/config.py

