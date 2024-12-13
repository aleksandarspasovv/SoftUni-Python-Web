from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TravelersHubApplication.travelers.urls')),
    path('', include('TravelersHubApplication.trips.urls')),
    path('', include('TravelersHubApplication.core.urls')),
]
