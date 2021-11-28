from django.urls import path
from rest_framework.routers import SimpleRouter

from constellations.views import *


router = SimpleRouter()
# router.register('constellations', ConstellationsViewSet)

urlpatterns = [
    path('constellations/', constellations_list),
    path('constellations/<int:pk>/', constellation_detail),
]
urlpatterns += router.urls
