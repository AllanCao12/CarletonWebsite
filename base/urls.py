from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # '' is the home directory
    path('clubEvents/', views.clubsEvents, name="clubEvents"),
    path('major/', views.major, name="major"),
    path('major/<str:pk>/', views.tips, name="majorAdvice"),
    path('clubEvents/create-event/', views.createEvent, name="createEvent"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]