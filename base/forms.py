from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event # What we're trying to make a form for
        fields = "__all__"
        exclude = ["clubName"]