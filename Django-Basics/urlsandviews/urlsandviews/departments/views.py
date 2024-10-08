from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def second_view(request, *args, **kwargs):
    return HttpResponse(f'<h1>Args: {args}, Kwargs: {kwargs} </h1>')


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')
