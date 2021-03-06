from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^project/rate/(\d+)$', views.rate, name='rate'),
    re_path(r'^new/project$', views.new_project, name='new_project'),
    re_path(r'^profile/(\d+)$', views.profile, name='profile'),
    re_path(r'^edit/profile', views.edit_profile, name='edit_profile'),
    re_path(r'^api/projects$', views.ProjectList.as_view()),
    re_path(r'^api/profiles$', views.ProfileList.as_view()),
]