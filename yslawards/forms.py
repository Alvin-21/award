from django import forms
from .models import *


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        exclude = ['critic', 'project']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
