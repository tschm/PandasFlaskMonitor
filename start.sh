#!/usr/bin/env bash
docker run -p 2058:8000 -v $(pwd)/frames/b:/frames:ro pdmonitor:latest