from rest_framework import serializers
from seats.models import SeatType
from charts.models import ChartSeats
from myauth.models import User



class SeatTypeSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    name = serializers.SlugRelatedField(slug_field='coordinates', queryset=ChartSeats.objects.all())


    class Meta:
        model = SeatType
        fields = ['id', 'name', 'created_by', 'created_on', 'color_code']

      
