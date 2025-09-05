from django.urls import path

from .views import example, say_hi_renad


urlpatterns = [
    path('', example),
    path('renad/', say_hi_renad)
]
