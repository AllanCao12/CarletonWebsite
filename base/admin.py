from django.contrib import admin

# Register your models here.
from . models import Major, Event

admin.site.register(Event)
admin.site.register(Major)