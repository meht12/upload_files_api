from django.urls import path
from .views  import  *
urlpatterns = [
     path('upload/', Files_UploadAPIView.as_view(), name='upload/'),
]