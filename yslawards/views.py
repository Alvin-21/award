from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.


def index(request):
    projects = Project.objects.all()
    ratings = Ratings.objects.all()
    avg_design = Ratings.average_design()
    avg_usability = Ratings.average_usability
    avg_content = Ratings.average_content
    form = RatingsForm()

    return render(request, 'index.html', {"projects": projects, "ratings": ratings, "avg_design": avg_design, "avg_usability": avg_usability, "avg_content": avg_content, "form": form})

@login_required(login_url='/accounts/login/')
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
        return HttpResponseRedirect(reverse('homepage'))

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('homepage')  
    else:
        form = ProjectForm()

    return render(request, 'new_project.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    current_user = request.user
    profile = Profile.objects.get(id=profile_id)
    projects = Project.objects.filter(user=current_user)
    return render(request, 'profile.html', {"profile": profile, "projects": projects})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')
    else:
        form = ProfileForm()

    return render(request, 'edit_profile.html', {"form": form})


class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
