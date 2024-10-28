from django.urls import path
from author.views import create_author_profile_view, author_details_view, edit_author_view, delete_author_view

urlpatterns = [
    path('create/', create_author_profile_view, name='create-author-profile'),
    path('details/', author_details_view, name='author-details'),
    path('authors/<int:pk>/edit/', edit_author_view, name='edit-author'),
    path('authors/<int:pk>/delete/', delete_author_view, name='delete-author'),

]
