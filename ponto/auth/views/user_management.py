from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from ponto.auth.serializers import UserSerializer


class UserManagementViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


user_management = UserManagementViewSet.as_view({
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'get': 'list'
})
