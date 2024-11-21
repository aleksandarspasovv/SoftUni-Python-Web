from django.urls import path
from liblaryApi.books import views

urlpatterns = [
    path('', views.index, name='index')
]