from django import forms
from TravelersHubApplication.travelers.models import Traveler


class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country', 'about_me']
