# Set the base image to Ubuntu
FROM continuumio/miniconda3

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

RUN conda install -q -y pandas flask

RUN pip install waitress

EXPOSE 8000

ADD . /pymonitor

WORKDIR /pymonitor

CMD python /pymonitor/start.py
