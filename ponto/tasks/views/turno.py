from rest_framework import viewsets
from ..models.Funcionario.turno import Turno
from ..serializers.Funcionario.turno import TurnoSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


turno = TurnoViewSet.as_view({
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'get': 'list'
})