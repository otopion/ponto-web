from ..models.Funcionario.turno import Turno
from ..serializers.Funcionario.turno import TurnoSerializer
from rest_framework import viewsets
from .funcionario import funcionario
from rest_framework.permissions import IsAuthenticated
from ponto.auth.permissions import IsActive
from ..models.Funcionario.funcionario import Funcionario
from django.http.request import HttpRequest


class TurnoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        self.queryset = Turno.objects.all()
        return self.queryset

    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated, IsActive]


turno = TurnoViewSet.as_view({
    'get': 'list'
})
