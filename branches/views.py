from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet , GenericViewSet
from .models import Branch
from .serializers import BranchSerializer


# Create your views here.

class BranchViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


