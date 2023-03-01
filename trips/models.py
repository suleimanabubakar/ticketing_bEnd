from django.db import models
from routes.models import Destination, End
from django.conf import settings
from seats.models import SeatType
from charts.models import ChartSeats
from accounting.models import Currency
# Create your models here.

class Trip(models.Model):
    start_at = models.ForeignKey(Destination, on_delete=models.CASCADE)
    end_at = models.ForeignKey(End, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expected_dep_time = models.DateTimeField()
    expected_arval_time = models.DateTimeField()

    def __str__(self):
        return f"{self.expected_dep_time.strftime('%m/%d/%Y %I:%M %p')} - {self.expected_arval_time.strftime('%m/%d/%Y %I:%M %p')}"


class TripDriver(models.Model):

    STATUS_PENDING = 'Pending'
    STATUS_PAID = 'Paid'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_PAID, 'Paid'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_on = models.DateTimeField()
    updated_by = models.CharField(max_length=255)   # ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_PENDING)

   
class TripDetails(models.Model):
    DEPARTURE = 'Departure'
    ARRIVAL = 'Arrival'
    STATE_CHOICES = [
        (DEPARTURE, 'Departure'),
        (ARRIVAL, 'Arrival'),
    ]

    trip = models.OneToOneField(Trip, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=255,  choices=STATE_CHOICES)  
    comments = models.CharField(max_length=500)

    class Meta:
        unique_together = ('trip', 'state')


class TripSeats(models.Model):
    trip_seats_involved = models.ForeignKey('TripSeatsInvolved', on_delete=models.CASCADE)
    seat = models.ForeignKey(ChartSeats, on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)



class TripSeatsInvolved(models.Model):
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('seat_type','trip')



class TripPricings(models.Model):
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    price = models.FloatField()
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)

