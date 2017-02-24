import unittest
import pandas as pd
import numpy as np


from web.app import app
from test.config import Config

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        frame = pd.DataFrame(data=np.random.randn(3, 10), index=["A", "B", "C"])
        self.app = app(Config, frame=frame)
        self.app = self.app.test_client()

    def tearDown(self):
        pass

    def testIndex(self):
        x = self.app.get('/')
        self.assertEqual(x.status_code, 200)

        x = self.app.get('/index')
        self.assertEqual(x.status_code, 200)
