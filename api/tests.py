from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse
import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import AIModel
from django.core.files.uploadedfile import SimpleUploadedFile

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

class AIModelAPITestCase(APITestCase):

    def setUp(self):
        # Create an instance of AIModel
        self.model_instance = AIModel.objects.create(
            name="Test Model",
            description="A test model.",
            num_classes=10,
            accuracy=99.99,
            macro_avg=99.9,
            wieghted_avg=99.8
        )
        self.model_file = SimpleUploadedFile("model.h5", b"file_content", content_type="application/octet-stream")
        self.model_instance.model_file.save("model.h5", self.model_file, save=True)

    def test_create_ai_model(self):
        url = "http://127.0.0.1:8000/api/models/"
        data = {
            'name': 'New AI Model',
            'description': 'This is a new model.',
            'num_classes': 5,
            'accuracy': 95.5,
            'macro_avg': 95.0,
            'wieghted_avg': 94.5,
            'model_file': SimpleUploadedFile("new_model.h5", b"new_file_content", content_type="application/octet-stream")
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AIModel.objects.count(), 2)

    def test_get_model_details(self):
        url = "http://127.0.0.1:8000/api/models/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['name'], 'Test Model')

    def test_update_ai_model(self):
        url = "http://127.0.0.1:8000/api/models/"
        data = {
            'description': 'Updated description.',
            'accuracy': 98.5
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.model_instance.refresh_from_db()
        self.assertEqual(self.model_instance.description, 'Updated description.')
        self.assertEqual(float(self.model_instance.accuracy), 98.5)

    def test_delete_ai_model(self):
        url = "http://127.0.0.1:8000/api/models/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AIModel.objects.count(), 0)

    def test_invalid_data_rejection(self):
        url = "http://127.0.0.1:8000/api/models/"
        data = {}  # Empty data should fail as name is required
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)