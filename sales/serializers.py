from rest_framework import serializers
from .models import Sale, Tickets

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['created_by', 'created_on', 'status', 'station', 'details']

class TicketsSerializer(serializers.ModelSerializer):
    sale = SaleSerializer()
    class Meta:
        model = Tickets
        fields = ['sale', 'seat', 'customer']