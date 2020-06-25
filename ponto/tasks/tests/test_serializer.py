from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models.Funcionario import Funcionario, Turno
from ..serializers.Funcionario import FuncionarioSerializer, TurnoSerializer


class SerializerTestCase(TestCase):
    user_class = get_user_model()

    def setUp(self):
        self.user = SerializerTestCase.user_class.objects.create_user(username='test-user', password='test-user')
        self.funcionario = Funcionario.objects.create(
            hora_saida="12:00",
            hora_chegada="18:00",
            user_id=self.user.pk
        )
        self.turno = Turno.objects.create(
            data="2020-04-02",
            hora_chegada="12:00",
            hora_saida="18:00",
            saida_almoco="15:00",
            entrada_almoco="15:30",
            presente=True,
            id_Funcionario_id=self.funcionario.pk
        )

    def test_funcionario_serializer(self):
        serializer = FuncionarioSerializer(self.funcionario)
        data = serializer.data
        self.assertIn('id', data)
        self.assertIn('hora_chegada', data)
        self.assertIn('hora_saida', data)
        self.assertIn('user', data)

    def test_turno_serializer(self):
        serializer = TurnoSerializer(self.turno)
        data = serializer.data
        self.assertIn('id', data)
        self.assertIn('hora_chegada', data)
        self.assertIn('hora_saida', data)
        self.assertIn('saida_almoco', data)
        self.assertIn('entrada_almoco', data)
        self.assertIn('presente', data)
        self.assertIn('id_Funcionario', data)
