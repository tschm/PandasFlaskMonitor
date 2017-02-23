#!/usr/bin/env bash
docker-compose build
docker-compose run -p "2004:8000" -d pymonitor
