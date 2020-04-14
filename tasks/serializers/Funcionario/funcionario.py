from tasks.models.Funcionario.funcionario import Funcionario
from rest_framework.serializers import ModelSerializer


class FuncionarioSerializer(ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
