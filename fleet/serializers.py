from rest_framework import serializers
from .models import Fleet, FleetChart
from myauth.models import User
from charts.models import ChartSeats

class FleetSerializers(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Fleet
        fields = ['name', 'plate_no', 'created_by', 'description']


class FleetChartSerializers(serializers.ModelSerializer):
    fleet = serializers.SlugRelatedField(slug_field='name', queryset=Fleet.objects.all())
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    chart_seats = serializers.SlugRelatedField(slug_field='coordinates', queryset=ChartSeats.objects.all())
    
    class Meta:
        model = FleetChart
        fields = ['fleet','created_by','created_on', 'chart_seats']

