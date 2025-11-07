from django.urls import path

from .views import (
    CreateOrderAPIView,
    ListOrderAPIView,
    DetailOrderAPIView
)

urlpatterns = [
    path('', ListOrderAPIView.as_view(), name='list-orders'),
    path('<int:pk>/', DetailOrderAPIView.as_view(), name='detail-order'),
    path('create/', CreateOrderAPIView.as_view(), name='create-order'),

    # path('categories/', ListCategoryAPIView.as_view(), name='list-categories'),
    # path('categories/<int:pk>/', DetailCategoryAPIView.as_view(), name='detail-category'),
    # path('categories/create/', CreateCategoryAPIView.as_view(), name='create-category'),
]
