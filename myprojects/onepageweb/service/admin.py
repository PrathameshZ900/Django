from django.contrib import admin
from service.models import ServiceItem

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title', 'dis')

admin.site.register(ServiceItem, ServiceAdmin)
# Register your models here.
