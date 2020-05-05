from .serializers import CadastrarSerializer
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model


class CadastrarView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CadastrarSerializer


cadastar = CadastrarView.as_view({
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'get': 'list'
})
