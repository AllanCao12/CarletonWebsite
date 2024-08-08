from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # '' is the home directory
    path('club-events/', views.clubsEvents, name="clubEvents"),
    path('major/', views.major, name="major"),
    path('club-events/create-event/', views.createEvent, name="createEvent"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('major/<slug:slug>/', views.MajorDetailView.as_view(), name='majorAdvice'),
    path('useful-links/', views.usefulLinks, name='usefulLinks'),
]