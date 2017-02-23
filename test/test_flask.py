import unittest



from web.app import app
from test.config import Config

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app(Config)
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