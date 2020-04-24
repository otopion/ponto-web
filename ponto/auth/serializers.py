from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, exceptions


class LoginRequestSerializer (serializers.Serializer):
    username = serializers.CharField(max_length=100, min_length=4)
    password = serializers.CharField()
    remember_me = serializers.BooleanField(default=False)

    def validate(self, attrs):
        """
        Nota: authenticate do ModelBackend não aceita logar
        usuários que tenham a flag is_active False, fazendo
        com que a função retorne None. Portanto,
        credenciais incorretas ou usuário não ativo resultará
        no mesmo código de erro.
        """

        user = authenticate(self.context['request'], **attrs)
        if user is None:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs


class LoginResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'groups',
            'user_permissions'
        ]
