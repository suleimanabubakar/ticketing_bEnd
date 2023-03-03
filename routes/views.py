from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet
from .models import Destination, Routes
from .serializers import DestinationSerializer, RoutesSerializer

# Create your views here.

class DestinationViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailsViewSet(RetrieveUpdateAPIView, GenericViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class RoutesViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class RoutesDetailsViewSet(RetrieveUpdateAPIView, GenericViewSet):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer
