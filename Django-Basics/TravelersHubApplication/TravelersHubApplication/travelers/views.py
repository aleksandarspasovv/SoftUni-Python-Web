from django.shortcuts import render, redirect
from TravelersHubApplication.travelers.forms import TravelerForm
from TravelersHubApplication.utils import get_user_obj


def create_traveler(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TravelerForm()
    return render(request, 'create-traveler.html', {'form': form})


def traveler_details(request):
    traveler = get_user_obj()

    if not traveler:
        return redirect('index')
    trips = traveler.trip_set.all().order_by('-start_date')

    return render(request, 'details-traveler.html', {'traveler': traveler, 'trips': trips})


def edit_traveler(request):
    traveler = get_user_obj()

    if not traveler:
        return redirect('index')

    if request.method == 'POST':
        form = TravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('traveler_details')
    else:
        form = TravelerForm(instance=traveler)

    return render(request, 'edit-traveler.html', {'form': form, 'traveler': traveler})


def delete_traveler(request):
    traveler = get_user_obj()

    if not traveler:
        return redirect('index')

    if request.method == 'POST':
        traveler.delete()
        return redirect('index')

    return render(request, 'delete-traveler.html', {'traveler': traveler})