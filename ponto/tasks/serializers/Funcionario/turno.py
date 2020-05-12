from ponto.tasks.models.Funcionario import Turno
from rest_framework import serializers


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = [
            "id",
            "data",
            "hora_chegada",
            "hora_saida",
            "saida_almoco",
            "entrada_almoco",
            "presente",
            "id_Funcionario",
        ]
