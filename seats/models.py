from django.db import models
from charts.models import ChartSeats
from django.conf import settings
from myauth.models import User

class SeatType(models.Model):
    name = models.ForeignKey(ChartSeats, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    color_code = models.CharField(max_length=150)

