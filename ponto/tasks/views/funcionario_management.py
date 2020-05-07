from rest_framework import viewsets
from ..models.Funcionario.funcionario import Funcionario
from ..serializers.Funcionario.funcionario import FuncionarioSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer


funcionario_ma = FuncionarioViewSet.as_view({
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'get': 'list'
})