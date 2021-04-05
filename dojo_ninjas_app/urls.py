from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojo/create', views.create_dojo),
    path('ninja/create', views.create_ninja),
]