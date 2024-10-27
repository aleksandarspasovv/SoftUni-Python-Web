# posts/urls.py
from django.urls import path
from posts.views import dashboard_view, create_post_view, post_details_view, edit_post_view, delete_post_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create/', create_post_view, name='create-post'),
    path('<int:post_id>/details/', post_details_view, name='post-detail'),
    path('<int:post_id>/edit/', edit_post_view, name='edit-post'),
    path('<int:post_id>/delete/', delete_post_view, name='delete-post'),
]
