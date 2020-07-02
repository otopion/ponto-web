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

    def validate_presente(self, value):
        data = self.get_initial()
        presente = data.get("hora_chegada")

        if value is True and presente is None:
            raise serializers.ValidationError("insira a hora de chegada")

        return value

