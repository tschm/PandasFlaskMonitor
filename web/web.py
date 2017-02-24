import logging
from flask import render_template
import pandas as pd


class Webserver(object):
    def __init__(self, table_format, frame, logger=None):
        self.__format = table_format
        self.__frame = frame
        self.__logger = logger or logging.getLogger(__name__)

    def __f2html(self, frame, name, tableformat):
        return frame.to_html(classes="{0} {1}".format(name, tableformat),
                             float_format=lambda x: '{0:.2f}'.format(x) if pd.notnull(x) else '-',
                             escape=False)

    def frame(self):
        self.__logger.debug(self.__frame)
        return render_template("frame.html", frame=self.__f2html(self.__frame.copy(), name="frame", tableformat=self.__format))


