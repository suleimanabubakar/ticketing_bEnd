from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['updated_on', 'updated_by', 'id_no','phone_number', 'full_names']