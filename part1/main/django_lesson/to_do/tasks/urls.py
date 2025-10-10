from django.urls import path

from .views import (
    all_to_do,
    change_status_to_in_progress,
    change_status_to_done
)


urlpatterns = [
    path('', all_to_do, name='all_to_do'),
    path('change-status-to-in-progress/<int:pk>/', change_status_to_in_progress, name='change_status_to_in_progress'),
    path('change-status-to-done/<int:pk>/', change_status_to_done, name='change_status_to_done'),

    # path('<int:pk>/', ..., name=...),
    # path('add/', ..., name=...),
]
