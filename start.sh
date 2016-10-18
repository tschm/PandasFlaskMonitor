#!/usr/bin/env bash
docker-compose build
docker-compose run -p "2002:5000" -d pymonitor
