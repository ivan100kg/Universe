from constellations.models import Constellation
from constellations.serializers import ConstellationSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def constellations_list(request):
    """
       List all code snippets, or create a new snippet.
       """
    if request.method == 'GET':
        constellations = Constellation.objects.all()
        serializer = ConstellationSerializer(constellations, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ConstellationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def constellation_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        constellation = Constellation.objects.get(pk=pk)
    except Constellation.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ConstellationSerializer(constellation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ConstellationSerializer(constellation, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        constellation.delete()
        return HttpResponse(status=204)

# from rest_framework import permissions
# from rest_framework.viewsets import ModelViewSet
#
#
# class ConstellationsViewSet(ModelViewSet):
#     queryset = Constellation.objects.all()
#     serializer_class = ConstellationSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]



