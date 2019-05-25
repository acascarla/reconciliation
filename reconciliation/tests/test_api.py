from rest_framework.test import APIClient
from django.test import SimpleTestCase


class ApiWorkTestCase(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_work_bad_request(self):
        response = self.client.get('/work/')
        self.assertEqual(response.status_code, 400)

    # TODO
    def test_work_not_found(self):
        response = self.client.get('/work/')
        self.assertEqual(response.status_code, 404)

    def test_work_retrieved(self):
        response = self.client.get('/work/')
        self.assertEqual(response.status_code, 200)
