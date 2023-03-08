from django.db import models
from django.conf import settings
from sales.models import Sale
from accounting.models import Currency

# Create your models here.


class Payment(models.Model):

    STATUS_PAID = 'Paid'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_PAID, 'Paid'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    sale = models.OneToOneField(Sale, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_PAID)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Focs(models.Model):
    amount = models.CharField(max_length=200)
    authorized_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    details = models.TextField()
    # sale = 
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class Discounts(models.Model):
    amount = models.CharField(max_length=200)
    details = models.TextField()
    # sale = 
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class CashPayment(models.Model):
    amount = models.CharField(max_length=200)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)


class MpesaPayment(models.Model):
    transaction = models.CharField(max_length=100)
    payment = models.ForeignKey(Payment, models.CASCADE)

