from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Chart, ChartSeats
from .serializers import ChartSerializer, ChartSeatsSerializer



# Create API views for Chart model
class ChartViewSet(CreateModelMixin,RetrieveModelMixin,DestroyModelMixin, ListModelMixin , GenericViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


# Create API views for ChartSeats model

class ChartSeatsViewSet(CreateModelMixin,RetrieveModelMixin ,DestroyModelMixin,ListModelMixin,  GenericViewSet):
    queryset = ChartSeats.objects.select_related('chart').all()
    serializer_class = ChartSeatsSerializer
    

# class ChartSeatsCreate(generics.CreateAPIView):
#     serializer_class = ChartSeatsSerializer

# class ChartSeatsDelete(generics.DestroyAPIView):
#     queryset = ChartSeats.objects.all()
#     serializer_class = ChartSeatsSerializer
#     lookup_field = 'id'
