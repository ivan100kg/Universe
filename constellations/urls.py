from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns


from constellations.views import *


router = SimpleRouter()
# router.register('constellations', ConstellationsViewSet)

urlpatterns = [
    path('constellations/', constellations_list),
    path('constellations/<int:pk>/', constellation_detail),
]
urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)

