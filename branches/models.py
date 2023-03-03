from django.db import models
from django.conf import settings

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    
