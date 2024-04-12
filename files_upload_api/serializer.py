from rest_framework import serializers
from .models import *


class Files_UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files_Upload
        fields = ['id','picture','uploaded_at']
