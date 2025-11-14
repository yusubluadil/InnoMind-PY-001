from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CreateOrderSerializer,
    ListOrderSerializer,
    DetailOrderSerializer
)
from ..models import Order


class CreateOrderAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [IsAuthenticated]


class ListOrderAPIView(generics.ListAPIView):
    serializer_class = ListOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user).order_by('-id')
        return queryset


class DetailOrderAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user=user)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        products = instance.products.all()
        for product in products:
            product.stock += 1
            product.save()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
