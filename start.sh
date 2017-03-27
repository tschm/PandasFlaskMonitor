#!/usr/bin/env bash
docker run -p 2058:8000 -v $(pwd)/frames/b:/pymonitor/frames:ro pdmonitor:latest