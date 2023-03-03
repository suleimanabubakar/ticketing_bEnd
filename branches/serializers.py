from rest_framework import serializers
from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'created_by', 'created_on']

