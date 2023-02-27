from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Chart(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
            return f"{self.name} - {self.created_by}"


class ChartSeats(models.Model):
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.chart} - {self.seat_no} - {self.coordinates}"
