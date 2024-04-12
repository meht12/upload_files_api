from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Files_Upload(models.Model):
    picture = models.ImageField(upload_to="upload_files",blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
