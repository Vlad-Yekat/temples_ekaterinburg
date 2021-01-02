from rest_framework import serializers
from core.models import City, Country, Church


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = '__all__'
