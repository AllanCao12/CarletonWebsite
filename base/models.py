from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    authors = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
