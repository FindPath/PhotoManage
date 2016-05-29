from django.shortcuts import render

# Create your views here.
from App.models import Album


def Home(request):
    a=Album.name