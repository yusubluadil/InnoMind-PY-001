from rest_framework import generics

from ..models import Book
from .serializers import (
    ListBookSerializer,
    DetailBookSerializer,
    CreateBookSerializer
)


class ListBookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ListBookSerializer


class DetailBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailBookSerializer


class CreateBookAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = CreateBookSerializer
