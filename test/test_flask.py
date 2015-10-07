import unittest
import os
import pandas as pd
import numpy as np

here = os.path.dirname(__file__)
os.environ["MONITOR_SETTINGS"] = os.path.join(here, "config.py")

from webserver import app, webserver
webserver.archive = pd.DataFrame(data=np.random.randn(3,10),index=["A","B","C"])


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app = self.app.test_client()

    def tearDown(self):
        pass

    def testIndex(self):
        x = self.app.get('/')
        self.assertEqual(x.status_code, 200)

        x = self.app.get('/index')
        self.assertEqual(x.status_code, 200)

    def testFrame(self):
        x = self.app.get('/frame')
        self.assertEqual(x.status_code, 200)

    def testFramex(self):
        x = self.app.get('/framex/A')
        self.assertEqual(x.status_code, 200)