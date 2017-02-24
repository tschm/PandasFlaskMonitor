import logging


class Config(object):
    logging.basicConfig(level=logging.DEBUG)
    HANDLER = [logging.StreamHandler()]
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "UY18980yn8892125"
    TESTING = False
    DEBUG = False
    TABLE_FORMAT = " table table-striped table-bordered table-hover"