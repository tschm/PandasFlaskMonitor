from waitress import serve
from web.app import app
from config.config import Config

if __name__ == '__main__':
    # It always run on port 8000 within the container.
    # You need to define the port the container will expose...
    serve(app(Config), port=8000)