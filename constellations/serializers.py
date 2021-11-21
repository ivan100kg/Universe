from rest_framework import serializers
from constellations.models import *


class ConstellationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Constellation
        fields = ['url', 'name', 'name_ru']
