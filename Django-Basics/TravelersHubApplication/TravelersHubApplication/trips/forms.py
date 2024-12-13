from django import forms
from TravelersHubApplication.trips.models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
