from django.urls import path
from . import views

urlpatterns = [
    path('traveler/create/', views.create_traveler, name='create_traveler'),
    path('traveler/details/', views.traveler_details, name='traveler_details'),
    path('traveler/edit/', views.edit_traveler, name='edit_traveler'),
    path('traveler/delete/', views.delete_traveler, name='delete_traveler'),
]
