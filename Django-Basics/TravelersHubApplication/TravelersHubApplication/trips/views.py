from django.shortcuts import render, redirect, get_object_or_404
from TravelersHubApplication.trips.models import Trip
from TravelersHubApplication.trips.forms import TripForm
from TravelersHubApplication.utils import get_user_obj


def all_trips(request):
    trips = Trip.objects.order_by('-start_date')
    return render(request, 'all-trips.html', {'trips': trips})


def create_trip(request):
    user_profile = get_user_obj()

    if not user_profile:
        return redirect('index')

    form = TripForm()

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.traveler = user_profile
            trip.save()
            return redirect('all_trips')

    return render(request, 'create-trip.html', {'form': form, 'user_profile': user_profile})


def trip_details(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    return render(request, 'details-trip.html', {'trip': trip})


def edit_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)

    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TripForm(instance=trip)

    return render(request, 'edit-trip.html', {'form': form, 'trip': trip})


def delete_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('all_trips')
    return render(request, 'delete-trip.html', {'trip': trip})
