from django.urls import path

from urlsandviews.departments.views import index, second_view, redirect_to_softuni

urlpatterns = [
    path('', index),
    path('softuni/', redirect_to_softuni),
    path('<param>/', second_view),

]