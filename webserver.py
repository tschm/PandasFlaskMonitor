#!./env/bin/python
import os
from flask import Flask
from web.web import Webserver

app = Flask(__name__)
here = os.path.dirname(__file__)

if not "MONITOR_SETTINGS" in os.environ:
    os.environ["MONITOR_SETTINGS"] = os.path.join(here, "config.py")

app.config.from_envvar("MONITOR_SETTINGS")
webserver = Webserver(table_format=app.config["TABLE_FORMAT"])


@app.route('/')
@app.route('/index')
def index():
    return webserver.index()

@app.route('/framex/<name>')
def framex(name):
    return webserver.framex(name)

@app.route('/frame')
def frame():
    return webserver.frame()

