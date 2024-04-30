from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import AIModel
from django.core.files.uploadedfile import SimpleUploadedFile
import json

class BasicAIAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_returns_empty_list(self):
        url = reverse('model-list')  # Use the named URL pattern
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
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


