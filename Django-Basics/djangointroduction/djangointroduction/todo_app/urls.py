from django.urls import path

from djangointroduction.todo_app.views import my_view, add_view

urlpatterns = [
    path('', my_view),
    path('add/', add_view)

]