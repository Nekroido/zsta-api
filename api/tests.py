import unittest

from pyramid import testing


class BaseViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()


class BaseFunctionalTests(unittest.TestCase):
    def setUp(self):
        from api import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)


class RootFunctionalTests(BaseFunctionalTests):
    def test_root(self):
        res = self.testapp.get('/', status=404, expect_errors=True)
        self.assertEqual(res.status_code, 404)

    def test_docs(self):
        res = self.testapp.get('/api', status=200, expect_errors=True)
        self.assertTrue(b'Swagger UI' in res.body)
