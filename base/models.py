from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    authors = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100, unique=False)
    description = models.TextField()
    clubName = models.CharField(max_length=100, unique=False, default="No Club")
    location = models.CharField(max_length=100, unique=False, default="Carleton University")
    date = models.DateField()
    
    def __str__(self):
        return self.name