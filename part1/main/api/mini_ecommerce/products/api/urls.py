from django.urls import path

from .views import (
    CreateCategoryAPIView,
    ListCategoryAPIView,
    DetailCategoryAPIView,
    CreateProductAPIView,
    ListProductAPIView,
    DetailProductAPIView,
)

urlpatterns = [
    path('', ListProductAPIView.as_view(), name='create-product'),
    path('<int:pk>/', DetailProductAPIView.as_view(), name='create-product'),
    path('create/', CreateProductAPIView.as_view(), name='create-product'),

    path('categories/', ListCategoryAPIView.as_view(), name='list-categories'),
    path('categories/<int:pk>/', DetailCategoryAPIView.as_view(), name='detail-category'),
    path('categories/create/', CreateCategoryAPIView.as_view(), name='create-category'),
]
