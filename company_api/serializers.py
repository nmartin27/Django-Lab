from rest_framework import serializers
from .models import Company
from .models import Location

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'industry',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('street', 'city', 'state',)