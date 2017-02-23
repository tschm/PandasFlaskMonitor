import pandas as pd
import numpy as np

class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "UY18980yn8892125"
    TESTING = False
    DEBUG = False
    TABLE_FORMAT = " table table-striped table-bordered table-hover"
    FRAME = pd.DataFrame(data=np.random.randn(3, 10), index=["A", "B", "C"])