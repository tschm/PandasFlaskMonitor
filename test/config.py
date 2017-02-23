import pandas as pd
import numpy as np

class Config(object):
    SECRET_KEY = "UY18980yn88921"
    TESTING = True
    DEBUG = True

    FRAME = pd.DataFrame(data=np.random.randn(3, 10), index=["A", "B", "C"])
    TABLE_FORMAT = " table table-striped table-bordered table-hover"
