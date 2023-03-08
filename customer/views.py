from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Customer
from .serializers import CustomerSerializer

# Create your views here.

class CustomerViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailsViewSet(RetrieveUpdateAPIView, GenericViewSet):
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer    
