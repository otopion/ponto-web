from tasks.models.Funcionario.turno import Turno
from rest_framework.serializers import ModelSerializer


class TurnoSerializer(ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'
