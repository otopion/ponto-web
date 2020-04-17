from django.contrib.auth import login as django_login
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ponto.auth.serializers import LoginRequestSerializer, LoginResponseSerializer

from ponto.tasks.models.Funcionario.funcionario import Funcionario

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginRequestSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            user = request.user
        else:
            serializer = self.get_serializer(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            django_login(request, user)
            remember_me = serializer.validated_data['remember_me']
            if not remember_me:
                request.session.set_expiry(0)
                request.session.modified = True
        return Response(LoginResponseSerializer(user).data)


login = LoginView.as_view()
