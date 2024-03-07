# models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=150)
    message = models.TextField()


# Create your models here.
