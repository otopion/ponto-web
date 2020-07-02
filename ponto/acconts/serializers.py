from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class CadastrarSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

    def validate_username(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Certifique-se de que este campo tenha mais de 4 caracteres.")
        return value

    def validate_password(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Certifique-se de que este campo tenha mais de 4 caracteres.")
        return value

    def validate_email(self, value):
        if value is "":
            raise serializers.ValidationError("Este campo não pode ser em branco.")
        return value
