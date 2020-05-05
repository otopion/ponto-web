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

