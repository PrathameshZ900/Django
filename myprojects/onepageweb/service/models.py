from django.db import models

# Create your models here.
class service(models.Model):
    icon = models.CharField(max_length = 10)
    title = models.CharField(max_length = 15)
    dis = models.TextField(max_length = 150)

    
    
    
