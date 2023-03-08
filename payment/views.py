from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView 
from rest_framework.viewsets import GenericViewSet
from .models import Payment, Focs, Discounts, CashPayment, MpesaPayment
from .serializers import PaymentSerializer, FocsSerializer, DiscountsSerializer, CashPaymentSerializer, MpesaPaymentSerializer

class PaymentViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class FocsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Focs.objects.all()
    serializer_class = FocsSerializer

class FocsDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = Focs.objects.all()
    serializer_class = FocsSerializer



class DiscountsViewSet(ListCreateAPIView, GenericViewSet):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer

class DiscountsDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer



class CashPaymentViewSet(ListCreateAPIView, GenericViewSet):
    queryset = CashPayment.objects.all()
    serializer_class = CashPaymentSerializer

class CashPaymentDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = CashPayment.objects.all()
    serializer_class = CashPaymentSerializer



class MpesaPaymentViewSet(ListCreateAPIView, GenericViewSet):
    queryset = MpesaPayment.objects.all()
    serializer_class = MpesaPaymentSerializer

class MpesaPaymentDetailViewSet(RetrieveAPIView, GenericViewSet):
    queryset = MpesaPayment.objects.all()
    serializer_class = MpesaPaymentSerializer
