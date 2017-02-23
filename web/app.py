from flask import Flask
from web.web import Webserver

def app(config):
    app_obj = Flask(__name__,template_folder="/pymonitor/templates", static_folder="/pymonitor/static")
    app_obj.config.from_object(config)
    webserver = Webserver(table_format=app_obj.config["TABLE_FORMAT"])
    webserver.archive = app_obj.config["FRAME"]

    @app_obj.route('/')
    @app_obj.route('/index')
    def index():
        return webserver.index()

    @app_obj.route('/framex/<name>')
    def framex(name):
        return webserver.framex(name)

    @app_obj.route('/frame')
    def frame():
        return webserver.frame()

    return app_obj


