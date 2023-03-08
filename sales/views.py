from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView 
from rest_framework.viewsets import GenericViewSet
from .models import Sale, Tickets
from .serializers import SaleSerializer, TicketsSerializer


# Create your views here.

class SaleViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class TicketsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer
    
class TicketsDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

