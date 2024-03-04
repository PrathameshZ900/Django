from django.db import models
from tinymce.models import HTMLField

class NewsArticle(models.Model):
    headline = models.CharField(max_length=35)
    dis = HTMLField()