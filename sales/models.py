from django.db import models
from django.conf import settings
from branches.models import Branch
from trips.models import TripSeats
from customer.models import Customer
# Create your models here.


class Sale(models.Model):

    STATUS_ACTIVE = 'Active'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    station = models.ForeignKey(Branch, on_delete=models.CASCADE)
    details = models.TextField()


class Tickets(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    seat = models.ForeignKey(TripSeats, on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
