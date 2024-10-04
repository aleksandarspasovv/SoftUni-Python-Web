from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def second_view(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args}, Kwargs: {kwargs} </h1>')