from rest_framework import serializers
from .models import Chart, ChartSeats
from myauth.models import User


class ChartSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Chart
        fields = ['name', 'created_on', 'created_by']

class ChartSeatsSerializer(serializers.ModelSerializer):
    chart = serializers.SlugRelatedField(slug_field='name', queryset=Chart.objects.all())
    class Meta:
        model = ChartSeats
        fields = ['chart', 'seat_no', 'coordinates']

 

