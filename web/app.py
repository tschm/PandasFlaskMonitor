from flask import Flask
from web.web import Webserver


def app(config, frame):
    app_obj = Flask(__name__, template_folder="/pymonitor/web/templates", static_folder="/pymonitor/web/static")
    app_obj.config.from_object(config)

    server = Webserver(table_format=app_obj.config["TABLE_FORMAT"], frame=frame, logger=app_obj.logger)

    @app_obj.route('/')
    @app_obj.route('/index')
    def index():
        return server.frame()

    return app_obj


