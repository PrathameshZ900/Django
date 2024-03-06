from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField 



class NewsArticle(models.Model):
    headline = models.CharField(max_length=35)
    dis = HTMLField()

    news_slug=AutoSlugField(populate_from='headline',unique=True,null=True,default=None)
    

    