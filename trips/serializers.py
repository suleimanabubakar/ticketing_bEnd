from rest_framework import serializers
from .models import Trip, TripDetails, TripDriver, TripPricings,TripSeats,TripSeatsInvolved

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['routes', 'created_on', 'created_by', 'expected_dep_time', 'expected_arval_time']

class TripDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDetails
        fields = ['trip', 'created_on', 'created_by', 'state', 'comments']
        

class TripDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripDriver
        fields = ['trip', 'driver', 'updated_on', 'updated_by', 'status']

class TripPricingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripPricings
        fields = ['seat_type','currency', 'price', 'updated_by', 'last_updated']

class TripSeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripSeats
        fields = ['trip_seats_involved', 'seat', 'status']

class TripSeatsInvolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripSeatsInvolved
        fields = ['seat_type', 'trip']
