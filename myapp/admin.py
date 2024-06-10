from django.contrib import admin
from .models import Client


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'contact', 'email', 'date']


admin.site.register(Client, ClientAdmin)

admin.site.site_title = ('CreativeTech')
admin.site.site_header = ('CreativeTech Administration')
