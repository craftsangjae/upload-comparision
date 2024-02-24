from django.urls import path
from .views import FileUploadView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('upload/',
         csrf_exempt(FileUploadView.as_view()), name='file_upload'),
]