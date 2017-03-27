#!/usr/bin/env python
from waitress import serve
from web.app import app
from config.config import Config
from frames.frame import frame

if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    serve(app(Config, frame=frame()), port=8000)