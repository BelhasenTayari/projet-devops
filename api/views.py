from rest_framework import generics
from .models import AIModel
from .serializers import AIModelSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
import os
from django.conf import settings
class AIModelListView(generics.ListAPIView):
    queryset = AIModel.objects.all()
    serializer_class = AIModelSerializer

