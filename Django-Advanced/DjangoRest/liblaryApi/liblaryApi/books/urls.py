from django.urls import path
from liblaryApi.books import views

urlpatterns = [
    path('', views.ListBookView.as_view(), name='index'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset')
]