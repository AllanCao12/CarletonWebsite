from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # '' is the home directory
]