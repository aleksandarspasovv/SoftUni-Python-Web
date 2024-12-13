from django.shortcuts import render

from TravelersHubApplication.utils import get_user_obj
from TravelersHubApplication.trips.models import Trip


def index(request):
    user_profile = get_user_obj()
    return render(request, 'index.html', {'user_profile': user_profile})