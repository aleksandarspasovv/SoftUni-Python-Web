from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello</h1>')


def second_view(request, *args, **kwargs):
    return HttpResponseNotFound()


def redirect_to_softuni(request):
    return redirect('https://softuni.bg/')
