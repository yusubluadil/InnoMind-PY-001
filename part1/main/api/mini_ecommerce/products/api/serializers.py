from rest_framework import serializers

from ..models import (
    Product,
    Category
)


class CreateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DetailCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# -------------------------------------------------------------------------- #


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ListProductSerializer(serializers.ModelSerializer):
    category = ListCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class DetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
