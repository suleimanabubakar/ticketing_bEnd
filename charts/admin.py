from django.contrib import admin
from .models import Chart, ChartSeats

# Register your models here.

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on', 'created_by'] 


@admin.register(ChartSeats)
class ChartSeatsAdmin(admin.ModelAdmin):
    list_display = ['chart', 'seat_no', 'coordinates'] 

