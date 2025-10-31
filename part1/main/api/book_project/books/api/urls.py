from django.urls import path

from .views import (
    ListBookAPIView,
    DetailBookAPIView,
    CreateBookAPIView
)

# localhost:8000/api/v1/books/ - List Book
# localhost:8000/api/v1/books/444/ - Detail, Update, Delete Book
# localhost:8000/api/v1/books/create/ - Create Book

urlpatterns = [
    path('', ListBookAPIView.as_view(), name='list_book'),
    path('<int:pk>/', DetailBookAPIView.as_view(), name='detail_book'),
    path('create/', CreateBookAPIView.as_view(), name='create_book'),
]