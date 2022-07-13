from rest_framework import serializers
from .models import Scheme


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheme
        fields = ['id', 'name']
