from django import forms
from .models import *


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['critic', 'project', 'pub_date']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
