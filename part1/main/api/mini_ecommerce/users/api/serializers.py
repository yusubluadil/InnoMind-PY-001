from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.contrib.auth.hashers import make_password

from ..models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password', 'check_password')

    def validate(self, attrs):
        pswd2 = attrs.pop('check_password')
        if attrs.get('password') != pswd2:
            raise ValidationError({'detail': 'Şifrələr eyni deyil.'})

        return super().validate(attrs)

    def create(self, validated_data):
        pswd = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.password = make_password(pswd)
        instance.save()

        return instance