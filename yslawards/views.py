from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    projects = Project.objects.all()
    ratings = Ratings.objects.all()
    form = RatingsForm()

    return render(request, 'index.html', {"projects": projects, "ratings": ratings,"form": form})


def rate(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user = request.user

    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.critic = user
            rating.project = project
            rating.save()
        return redirect('home')


def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')  
    else:
        form = ProjectForm()

    return render(request, 'project.html', {'form': form})