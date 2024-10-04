from django.urls import path

from urlsandviews.departments.views import index, second_view

urlpatterns = [
    path('', index),
    path('<param>/', second_view)
]