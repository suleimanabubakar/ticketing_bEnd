from django.db import models
from branches.models import Branch
from django.conf import settings

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
            return f"{self.name} - {self.created_by}"

class Routes(models.Model):
    start_point = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="start")
    end_point = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="end")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
            return f"{self.start_point} - {self.end_point} - {self.created_by}"