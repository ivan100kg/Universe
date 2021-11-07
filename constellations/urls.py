from django.urls import path

from constellations.views import ConstellationsListView

urlpatterns = [
    path('', ConstellationsListView.as_view(), name='constellations_list'),
]