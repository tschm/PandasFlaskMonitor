from flask import render_template, url_for
import pandas as pd


class Webserver(object):
    def __init__(self, table_format):
        self.__format = table_format

    def __f2html(self, frame, name, tableformat):
        return frame.to_html(classes="{0} {1}".format(name, tableformat),
                             float_format=lambda x: '{0:.2f}'.format(x) if pd.notnull(x) else '-',
                             escape=False)

    def __link(self, endpoint, values):
        rows = [(url_for(endpoint=endpoint, _external=True, **v[1]), v[0]) for v in values]
        return ['<a href={0}>{1}</a>'.format(row[0], row[1]) for row in rows]

    @property
    def archive(self):
        return self.__frame

    @archive.setter
    def archive(self, value):
        self.__frame = value


    def framex(self, name):
        return render_template("frame.html", frame=self.__f2html(pd.DataFrame(self.__frame.ix[name]), name="frame", tableformat=self.__format))

    def frame(self):
        frame = self.__frame.copy()
        values = [(name, {"name": name}) for name in frame.index]
        frame.index = self.__link("framex", values)

        return render_template("frame.html", frame=self.__f2html(frame, name="frame", tableformat=self.__format))

    def index(self):
        return render_template("index.html")

