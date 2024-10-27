# posts/urls.py
from django.urls import path
from posts.views import dashboard_view, create_post_view, post_details_view, edit_post_view, delete_post_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create/', create_post_view, name='create-post'),
    path('posts/<int:pk>/', post_details_view, name='post-details'),
    path('posts/<int:pk>/edit/', edit_post_view, name='edit-post'),
    path('posts/<int:pk>/delete/', delete_post_view, name='delete-post'),
]
