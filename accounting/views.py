from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import GenericViewSet
from .models import Currency
from .serializers import CurrencySerializer

# Create your views here.

class CurrencyViewSet( ListCreateAPIView, GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyDetailViewSet(RetrieveUpdateAPIView, GenericViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer