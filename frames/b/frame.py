import os
import pandas as pd

base_dir = os.path.dirname(__file__)

def frame():
    return pd.read_csv(os.path.join(base_dir, "b.csv"), index_col=0)