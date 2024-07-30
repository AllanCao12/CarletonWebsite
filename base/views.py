from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Major, Event
from .forms import EventForm

# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def clubsEvents(request):
    Events = Event.objects.all()
    context = {'events': Events}
    return render(request, 'base/clubEvents.html', context)

def major(request):
    Majors = Major.objects.all()
    context = {"Majors": Majors}
    return render(request, 'base/majors.html', context)

def tips(request):
    context = {}
    return render(request, 'base/tips.html', context)

def createEvent(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.clubName = request.user # automatically sets the user to whoever made the room
            event.save()
            
            return redirect("clubEvents")
        
    context = {'form': form}
    return render(request, "base/eventForm.html", context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")   
    context = {}
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')