from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^/project/rate/(\d+)$', views.rate, name='rate'),
]