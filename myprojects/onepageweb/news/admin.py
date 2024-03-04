from django.contrib import admin
from news.models import NewsArticle




class newsc(admin.ModelAdmin):
    list_display = ('headline', 'dis')

admin.site.register(NewsArticle, newsc)
# Register your models here.
