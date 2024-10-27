# RegularExam/urls.py
from django.contrib import admin
from django.urls import path, include
from posts.views import index_view  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),  # Route for the home page
    path('author/', include('author.urls')),  # Author URLs
    path('posts/', include('posts.urls')),    # Post URLs
]
