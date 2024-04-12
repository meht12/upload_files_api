from django.contrib import admin
from .models import *
# Register your models here.


class profileAdmin(admin.ModelAdmin):
    list_display = ['picture',] 
    
    admin.site.register(Files_Upload)
