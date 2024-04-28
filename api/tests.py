from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
import json

class BasicAIAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_returns_empty_list(self):
        
        
        response = self.client.get("http://127.0.0.1:8000/api/models/")

        # Assert status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Parse response content as JSON
        data = json.loads(response.content)

        # Assert that the response contains an empty list
        self.assertEqual(data, [])