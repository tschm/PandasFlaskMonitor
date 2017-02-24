import pandas as pd
import numpy as np

def frame():
    return pd.DataFrame(data=np.random.randn(3, 10), index=["A", "B", "C"])