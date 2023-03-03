from django.contrib import admin
from .models import Destination, Routes

# Register your models here.

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'branch','created_on', 'created_by'] 
