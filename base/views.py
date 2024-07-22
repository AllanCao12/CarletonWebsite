from django.shortcuts import render
from django.http import HttpResponse
from .models import Major

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def clubsEvents(request):
    context = {}
    return render(request, 'base/clubEvents.html', context)

def major(request):
    Majors = Major.objects.all()
    context = {"Majors": Majors}
    return render(request, 'base/majors.html', context)

def tips(request):
    context = {}
    return render(request, 'base/tips.html', context)