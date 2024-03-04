from django.db import models

class ServiceItem(models.Model):
    icon = models.CharField(max_length=20)
    title = models.CharField(max_length=15)
    dis = models.TextField(max_length=150)

    
