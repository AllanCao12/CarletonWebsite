from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.detail import DetailView

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

def usefulLinks(request):
    context = {}
    return render(request, 'base/usefulLinks.html', context)

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

class MajorDetailView(DetailView):
    model = Major # The model we want to use to fill out the template with
    template_name = 'base/tips.html' # The template
    context_object_name = 'major' # The name of the model we will use in the template to access the values
    slug_field = 'slug' # The value in the model that we're looking for
    slug_url_kwarg = 'slug' # The value in the url that we're comparing to the slug_field in the model to retrieve the correct model