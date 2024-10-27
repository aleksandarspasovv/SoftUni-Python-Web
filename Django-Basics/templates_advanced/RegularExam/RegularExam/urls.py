from django.contrib import admin
from django.urls import path, include
from posts.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='home'),
    path('author/', include('author.urls')),
    path('posts/', include('posts.urls')),
]
