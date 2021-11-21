from rest_framework import serializers
from constellations.models import *


class ConstellationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constellation
        fields = ["name_ru", "square", "total_stars"]
