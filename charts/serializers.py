from .models import Chart, ChartSeats
from rest_framework import serializers


class ChartSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Chart
        fields = '__all__'

class ChartSeatsSerializer(serializers.ModelSerializer):
    chart = serializers.SerializerMethodField()
    class Meta:
        model = ChartSeats
        fields = '__all__'

    def get_chart(self, obj):
        chart = obj.chart
        return f"{chart.name} ({chart.id})" if chart else None

