from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from constellations.models import Constellation
from dataparser.wiki_parser import main


class ConstellationsListView(ListView):
    model = Constellation



