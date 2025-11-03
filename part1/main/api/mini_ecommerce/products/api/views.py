from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .filters import ProductFilter
from .permissions import IsAdminOrReadOnly
from .serializers import (
    CreateCategorySerializer,
    ListCategorySerializer,
    DetailCategorySerializer,
    CreateProductSerializer,
    ListProductSerializer,
    DetailProductSerializer
)
from ..models import (
    Product,
    Category
)


class CreateCategoryAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CreateCategorySerializer
    permission_classes = [IsAdminUser]


class ListCategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer


class DetailCategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = DetailCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

# ----------------------------------------------------------------------- #

class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAdminUser]


class ListProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'name']


class DetailProductAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DetailProductSerializer
    permission_classes = [IsAdminOrReadOnly]
