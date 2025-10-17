from django.urls import path

from .views import (
    all_to_do,
    change_status_to_in_progress,
    change_status_to_done,
    add_to_do,
    detail_to_do,
    search_to_do,
    delete_to_do
)


urlpatterns = [
    path('', all_to_do, name='all_to_do'),
    path('change-status-to-in-progress/<int:pk>/', change_status_to_in_progress, name='change_status_to_in_progress'),
    path('change-status-to-done/<int:pk>/', change_status_to_done, name='change_status_to_done'),

    path('<int:pk>/', detail_to_do, name='detail_to_do'),
    path('delete/<int:pk>/', delete_to_do, name='delete_to_do'),
    path('add/', add_to_do, name='add_to_do'),
    path('search-to-do/', search_to_do, name='search_to_do'),
]
