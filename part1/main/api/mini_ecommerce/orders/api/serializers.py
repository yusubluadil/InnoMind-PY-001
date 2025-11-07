from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.db import transaction

from products.api.serializers import ListProductSerializer
from ..models import Order


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('products',)

    def create(self, validated_data):
        with transaction.atomic():
            user = self.context['request'].user
            products = validated_data.get('products', [])
            total_price = 0
            for product in products:
                total_price += product.price
                product.stock -= 1
                product.save()

            validated_data['total_price'] = total_price
            validated_data['user'] = user

            return super().create(validated_data)
        raise ValidationError({'detail': 'Gözlənilməyən xəta baş verdi.'})


class ListOrderSerializer(serializers.ModelSerializer):
    products = ListProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'total_price', 'created_at', 'products')


class DetailOrderSerializer(serializers.ModelSerializer):
    products = ListProductSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(max_digits=8, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'total_price', 'created_at', 'products')
