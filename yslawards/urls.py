from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^project/rate/(\d+)$', views.rate, name='rate'),
    re_path(r'^new/project$', views.new_project, name='new_project'),
    re_path(r'^profile/(\d+)$', views.profile, name='profile'),
]