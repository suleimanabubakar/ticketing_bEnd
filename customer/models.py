from django.db import models
from django.conf import settings
# Create your models here.

# CUSTOMER
# UPDATED ON
# UPDATED BY
# ID NO (NULL == TRUE)
# PHONE NO
# FULL NAMES

class Customer(models.Model):
    updated_on = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_no = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=20)
    full_names = models.CharField(max_length=255)