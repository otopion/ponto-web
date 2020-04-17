from ponto.tasks.models.Funcionario import Funcionario
from rest_framework.serializers import ModelSerializer


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = [
            'hora_chegada',
            'hora_saida',
        ]
