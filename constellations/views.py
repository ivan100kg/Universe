from django.shortcuts import render
from django.views.generic import ListView

from constellations.models import Constellation


class ConstellationsListView(ListView):
    model = Constellation
