from rest_framework.test import APIClient
from django.core import management
from django.test import TestCase


class ApiWorkTestCase(TestCase):

    def setUp(self):
        management.call_command('import_works_metadata')
        self.client = APIClient()

    def test_work_bad_request(self):
        response = self.client.get('/work/')
        self.assertEqual(response.status_code, 400)

    def test_work_not_found(self):
        response = self.client.get('/work/?iswc=not_valid_iswc')
        self.assertEqual(response.status_code, 404)

    def test_work_retrieved(self):
        response = self.client.get('/work/?iswc=T9204649558')
        self.assertEqual(response.status_code, 200)
        expected_data = {
            'contributors': [{
                'name': 'Edward Christopher Sheeran',
            }],
            'title': 'Shape of You',
            'iswc': 'T9204649558',
        }
        self.assertEqual(response.data['title'], expected_data['title'])
        self.assertEqual(response.data['iswc'], expected_data['iswc'])
        self.assertEqual(1, len(expected_data['contributors']))
        self.assertEqual(
            response.data['contributors'][0]['name'],
            expected_data['contributors'][0]['name'],
        )
