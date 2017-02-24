# Set the base image to Ubuntu
FROM continuumio/miniconda3

# File Author / Maintainer
MAINTAINER Thomas Schmelzer "thomas.schmelzer@gmail.com"

RUN conda install -q -y pandas flask

RUN pip install waitress

EXPOSE 8000

ADD ./start.py   /pymonitor/start.py
ADD ./config     /pymonitor/config
ADD ./static     /pymonitor/static
ADD ./templates  /pymonitor/templates
ADD ./web        /pymonitor/web

WORKDIR /pymonitor

CMD python /pymonitor/start.py
