from ..models.Funcionario.turno import Turno
from ..serializers.Funcionario.turno import TurnoSerializer
from rest_framework.viewsets import ModelViewSet


class TurnoViewSet(ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


turno_ma = TurnoViewSet.as_view({
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
    'get': 'list'
})
