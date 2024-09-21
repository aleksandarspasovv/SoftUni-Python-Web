from django import http
from django.shortcuts import render

# Create your views here.

def my_view(request):
    return http.HttpResponse("<h1>Hello!</h1>")