from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from ponto.auth.permissions import IsActive
from ponto.tasks.serializers.Funcionario.funcionario import FuncionarioSerializer
from ..models.Funcionario.funcionario import Funcionario
from rest_framework import viewsets


class FuncionarioView(viewsets.ModelViewSet):

    def get_queryset(self):
        self.queryset = Funcionario.objects.filter(user=self.request.user.id)
        return self.queryset

    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated, IsActive]


funcionario = FuncionarioView.as_view({
    'get': 'list'
})
