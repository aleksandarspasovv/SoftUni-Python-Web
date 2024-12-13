from django.http import HttpResponse


def view_counter(request):
    request.session['counter'] = request.session.get('counter', 0) + 1

    return HttpResponse(f'the count is {request.session.get("counter")}')
