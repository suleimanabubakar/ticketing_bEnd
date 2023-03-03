from rest_framework import serializers
from .models import Destination, Routes

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['name', 'branch', 'created_by', 'created_on']

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = ['start_point', 'end_point', 'created_by', 'created_on']

