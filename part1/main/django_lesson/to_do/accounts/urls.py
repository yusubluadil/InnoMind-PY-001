from django.urls import path

from .views import (
    user_login,
    register,
    profile,
    logout_view
)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]
