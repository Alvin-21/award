from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.


def index(request):
    projects = Project.objects.all()
    ratings = Ratings.objects.all()
    form = RatingsForm()

    return render(request, 'index.html', {"form": form})


def rate(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    user = request.user

    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            text = form.cleaned_data['text']
            review = form.save(commit=False)
            rating = Ratings(critic=user, project=project, design=design, usability=usability, content=content, text=text)
            rating.save()
            return redirect('home')
