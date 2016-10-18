#!./env/bin/python
import pandas as pd
from flask import Flask
from web.web import Webserver

app = Flask(__name__)
app.config.from_envvar("WEBSERVER_SETTINGS")
webserver = Webserver(table_format=app.config["TABLE_FORMAT"])
webserver.archive = pd.DataFrame(index=[0,1],columns=["A","B"])

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

if __name__ == "__main__":
    app.logger.info("Main")
    app.run()