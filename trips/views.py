from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet
from .models import Trip, TripDetails, TripDriver, TripPricings, TripSeats, TripSeatsInvolved
from .serializers import TripSerializer, TripDetailsSerializer, TripDriverSerializer, TripPricingsSerializer, TripSeatsSerializer, TripSeatsInvolvedSerializer

# Create your views here.

class TripViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetailsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = TripDetails.objects.all()
    serializer_class = TripDetailsSerializer


class TripDriverViewSet(ListCreateAPIView, GenericViewSet):
    queryset = TripDriver.objects.all()
    serializer_class = TripDriverSerializer

class TripPricingsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = TripPricings.objects.all()
    serializer_class = TripPricingsSerializer
    
class TripSeatsInvolvedViewSet(ListCreateAPIView, GenericViewSet):
    queryset = TripSeatsInvolved.objects.all()
    serializer_class = TripSeatsInvolvedSerializer

class TripSeatsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = TripSeats.objects.all()
    serializer_class = TripSeatsSerializer

