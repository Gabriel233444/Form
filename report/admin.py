from django.contrib import admin
from .models import Form, FileUpload

admin.site.register(Form)
admin.site.register(FileUpload)