from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Fleet, FleetChart
from .serializers import FleetSerializers, FleetChartSerializers

# Create your views here.

class FleetViewSet(ModelViewSet):
    queryset = Fleet.objects.all()
    serializer_class = FleetSerializers

class FleetChartViewSet(ModelViewSet):
    queryset = FleetChart.objects.all()
    serializer_class = FleetChartSerializers
