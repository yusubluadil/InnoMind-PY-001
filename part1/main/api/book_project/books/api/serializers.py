from rest_framework import serializers

from ..models import Book


class ListBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class DetailBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('created_at',)


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('created_at', 'is_available')
