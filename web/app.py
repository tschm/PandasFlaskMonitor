from flask import Flask
from web.web import Webserver

def app(config, frame):
    app_obj = Flask(__name__,template_folder="/pymonitor/templates", static_folder="/pymonitor/static")
    app_obj.config.from_object(config)
    for handler in app_obj.config["HANDLER"]:
        app_obj.logger.addHandler(handler)

    server = Webserver(table_format=app_obj.config["TABLE_FORMAT"], frame=frame, logger=app_obj.logger)

    @app_obj.route('/')
    @app_obj.route('/index')
    def index():
        app_obj.logger.debug("main routine")
        return server.frame()

    return app_obj


