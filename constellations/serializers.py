from rest_framework import serializers
from constellations.models import *
from django.contrib.auth.models import User


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        # fields = ['id', 'name', 'name_ru']
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    constellations = serializers.PrimaryKeyRelatedField(many=True, queryset=Constellation.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'constellations']
