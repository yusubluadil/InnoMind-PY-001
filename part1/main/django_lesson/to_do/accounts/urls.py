from django.urls import path

from .views import (
    logout_view
)


urlpatterns = [
    # path('register/', ..., name=...),
    # path('login/', ..., name=...),
    path('logout/', logout_view, name='logout'),
]
