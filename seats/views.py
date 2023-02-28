from django.shortcuts import render
from rest_framework.viewsets import  ModelViewSet
from .models import SeatType
from .serializers import SeatTypeSerializer

# Create your views here.

class SeatTypeViewSet(ModelViewSet):
    queryset = SeatType.objects.all()
    serializer_class = SeatTypeSerializer

