from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from ..models.Funcionario.funcionario import Funcionario
from ..models.Funcionario.turno import Turno


class ModelTestCase(TestCase):
    user_class = get_user_model()

    def setUp(self):
        self.user = ModelTestCase.user_class.objects.create_user(username='test-user', password='test-user')
        Funcionario.objects.create(
            hora_chegada="12:00",
            hora_saida="18:00",
            user_id=self.user.pk,
        )
        self.fun = Funcionario.objects.get(user_id=self.user.pk)
        Turno.objects.create(
            data="2020-04-02",
            hora_chegada="12:00",
            hora_saida="18:00",
            saida_almoco="15:00",
            entrada_almoco="15:30",
            presente=True,
            id_Funcionario_id=self.fun.pk
        )

    def test_user_in_funcionario(self):
        self.assertEqual(self.user.pk, self.fun.user_id)

    def test_funcionario_in_turno(self):
        turno = Turno.objects.get(id_Funcionario_id=self.fun.pk)
        self.assertEqual(self.fun.pk, turno.id_Funcionario_id)

    def test_exist_funcionario(self):
        self.assertTrue(Funcionario.objects.exists())

    def test_exist_turno(self):
        self.assertTrue(Turno.objects.exists())



