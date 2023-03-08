from rest_framework import serializers
from .models import Payment, Focs, Discounts, CashPayment, MpesaPayment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['sale', 'status', 'currency']
        
class FocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focs
        fields = ['amount', 'authorized_by', 'details', 'payment']


class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = ['amount', 'details', 'payment']


class CashPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashPayment
        fields = ['amount', 'currency', 'payment']


class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields = ['transaction', 'payment']