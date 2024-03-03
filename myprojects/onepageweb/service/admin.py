from django.contrib import admin
from service.models import service

class serviceAdmin(admin.ModelAdmin):
    list_display=('icon','title','dis')


admin.site.register(service,serviceAdmin)


# Register your models here.
