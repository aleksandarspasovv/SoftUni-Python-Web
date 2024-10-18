from django.urls import path
from forumApp.posts.views import index

urlpatterns = [
    path('', index, name='index')
]
