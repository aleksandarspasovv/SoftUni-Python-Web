from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    context = {
        'current_time': datetime.now(),
        'some_text': 'I am the best programmer',
    }

    return render(request, 'base.html', context=context)
