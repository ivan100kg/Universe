from rest_framework import serializers
from constellations.models import *


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        # fields = ['id', 'name', 'name_ru']
        fields = '__all__'
