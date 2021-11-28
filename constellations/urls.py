from django.urls import path
from rest_framework.routers import SimpleRouter

from constellations.views import *


router = SimpleRouter()
# router.register('constellations', ConstellationsViewSet)

urlpatterns = [
    path('', constellations_list)
]
urlpatterns += router.urls
