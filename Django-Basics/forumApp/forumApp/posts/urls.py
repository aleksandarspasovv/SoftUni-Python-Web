from django.urls import path, include
from forumApp.posts.views import dashboard, add_post, delete_post, details_page, edit_post, Index, RedirectHomeView, \
    DashboardView, AddPostView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dash'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', delete_post, name='delete-post'),
        path('details-post/', details_page, name='details-post'),
        path('edit-post/', edit_post, name='edit-post'),
    ])),
    path('redirect-home', RedirectHomeView.as_view(), name='redirect-home'),
]