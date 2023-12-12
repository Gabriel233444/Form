from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supervisor = models.CharField(max_length=20, default='The Chairman')
    monday = models.CharField(max_length=100)
    tuesday = models.CharField(max_length=100)
    wednessday = models.CharField(max_length=100)
    thursday = models.CharField(max_length=100)
    friday = models.CharField(max_length=100)
    monday1 = models.CharField(max_length=100)
    tuesday1 = models.CharField(max_length=100)
    wednessday1 = models.CharField(max_length=100)
    thursday1 = models.CharField(max_length=100)
    friday1 = models.CharField(max_length=100)
    projects = models.IntegerField()
    study_materials = models.IntegerField()
    rating = models.IntegerField()
    challenges = models.CharField(max_length=100)
    monday2 = models.TimeField()
    tuesday2 = models.TimeField()
    wednessday2 = models.TimeField()
    thursday2 = models.TimeField()
    friday2 = models.TimeField()
    whatsapp = models.IntegerField()
    facebook = models.IntegerField()
    twitter = models.IntegerField()
    instagram = models.IntegerField()
    monday3 = models.CharField(max_length=100)
    tuesday3 = models.CharField(max_length=100)
    wednessday3 = models.CharField(max_length=100)
    thursday3 = models.CharField(max_length=100)
    friday3 = models.CharField(max_length=100) 
    sugestions = models.CharField(max_length=100)   
    total_weeks = models.CharField(max_length=20)
    monday4 = models.IntegerField()
    tuesday4 = models.IntegerField()
    wednessday4 = models.IntegerField()
    thursday4 = models.IntegerField()
    friday4 = models.IntegerField()
    
class FileUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to='files/')
    
    def extension(self):
        _, file_extension = os.path.splitext(self.files.name)
        return file_extension