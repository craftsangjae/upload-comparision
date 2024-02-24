from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UploadFile

class FileUploadView(CreateView):
    model = UploadFile
    fields = ['file', ]
    success_url = '/'
    template_name = 'uploadapp/file_form.html'