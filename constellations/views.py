from rest_framework.viewsets import ModelViewSet
from constellations.models import Constellation
from constellations.serializers import ConstellationSerializer


class ConstellationsViewSet(ModelViewSet):
    queryset = Constellation.objects.all()
    serializer_class = ConstellationSerializer



