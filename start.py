#!/usr/bin/env python
from waitress import serve
from web.app import app
from config.config import Config


if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    import importlib.util
    spec = importlib.util.spec_from_file_location("frame", "/frames/frame.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    frame = foo.frame()

    serve(app(Config, frame=frame), port=8000)