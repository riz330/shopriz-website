from email import message
from django.db import models
# from django.contrib import messages
# from requests import request

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=22)
    email=models.CharField(max_length=22)
    subject=models.CharField(max_length=22)
    message=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name    