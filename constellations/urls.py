from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns


from constellations.views import *


router = SimpleRouter()
# router.register('constellations', ConstellationsViewSet)

urlpatterns = [
    path('constellations/', ConstellationsList.as_view()),
    path('constellations/<int:pk>/', ConstellationDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)

