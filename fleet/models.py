from django.db import models
from charts.models import ChartSeats
from django.conf import settings


class Fleet(models.Model):
    name = models.CharField(max_length=255)
    plate_no = models.CharField(max_length=20)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

class FleetChart(models.Model):
    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    chart_seats = models.ForeignKey(ChartSeats, on_delete=models.CASCADE)
