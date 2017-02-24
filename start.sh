#!/usr/bin/env bash
docker build --tag=pdmonitor .
docker run -p 2058:8000 -v $(pwd)/frames/b:/frames:ro pdmonitor:latest