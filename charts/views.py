from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import Chart, ChartSeats
from .serializers import ChartSerializer, ChartSeatsSerializer



# Create API views for Chart model
class ChartViewSet(ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer


# Create API views for ChartSeats model

class ChartSeatsViewSet(CreateModelMixin,RetrieveModelMixin ,DestroyModelMixin,ListModelMixin,  GenericViewSet):
    queryset = ChartSeats.objects.all()
    serializer_class = ChartSeatsSerializer
    


