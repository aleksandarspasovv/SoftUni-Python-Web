from django import http
from django.shortcuts import render

from djangointroduction.todo_app.models import Task


# Create your views here.

def my_view(request):
    return http.HttpResponse("<h1>Obicham Bebo!</h1>")


def add_view(request):
    return http.HttpResponse("<h1>Mnogo Obicham Bebe Mace</h1>")


def advanced_view(result):
    tasks = Task.objects.all()

    result = [
        "<h1>TASKS</h1>",
        '<ul>',
        *[f"<li>{task.name}</li>" for task in tasks],
        '</ul>',
    ]

    return http.HttpResponse(result)
