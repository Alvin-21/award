from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    projects = Project.objects.all()
    ratings = Ratings.objects.all()
    form = RatingsForm()

    return render(request, 'index.html', {"form": form})


