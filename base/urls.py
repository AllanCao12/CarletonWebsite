from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # '' is the home directory
    path('clubEvents/', views.clubsEvents, name="clubEvents"),
    path('major/', views.major, name="major"),
    path('major/<str:pk>/', views.tips, name="majorAdvice")
]