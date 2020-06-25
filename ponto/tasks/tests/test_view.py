from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

from ..models.Funcionario.funcionario import Funcionario
from ..models.Funcionario.turno import Turno


class ViewTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='username',
            password='password'
        )
        self.user_no_active = get_user_model().objects.create_user(
            username='user_no_active',
            password='user_no_active',
            is_active=False
        )
        self.funcionario = Funcionario.objects.create(
            hora_chegada="12:00",
            hora_saida="18:00",
            user_id=self.user.pk
        )
        self.turno = Turno.objects.create(
            data='2020-02-05',
            hora_chegada='12:00',
            hora_saida='18:00',
            saida_almoco='15:00',
            entrada_almoco='15:30',
            presente=True,
            id_Funcionario_id=self.funcionario.pk
        )

    def test_get_funcionario(self):
        self.client.login(username='username', password='password')

        response = self.client.get(reverse('tasks:funcionario'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, self.funcionario.hora_chegada)
        self.assertContains(response, self.funcionario.hora_saida)
        self.assertContains(response, self.funcionario.user_id)

    def test_get_turno(self):
        self.client.login(username='username', password='password')

        response = self.client.get(reverse('tasks:turno'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, self.turno.data)
        self.assertContains(response, self.turno.hora_chegada)
        self.assertContains(response, self.turno.hora_saida)
        self.assertContains(response, self.turno.saida_almoco)
        self.assertContains(response, self.turno.entrada_almoco)
        self.assertTrue(response, self.turno.presente)
        self.assertContains(response, self.turno.id_Funcionario_id)

    def test_get_fail_funcionario(self):
        self.client.login(username='user_no_activ', password='user_no_activ')

        response = self.client.get(reverse('tasks:funcionario'))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_fail_turno(self):
        self.client.login(username='user_no_activ', password='user_no_activ')

        response = self.client.get(reverse('tasks:turno'))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_turno(self):
        data = {
            'data': '2020-02-05',
            'hora_chegada': '12:00',
            'hora_saida': '18:00',
            'saida_almoco': '15:00',
            'entrada_almoco': '15:30',
            'presente': True,
            'id_Funcionario': self.funcionario.pk
        }
        response = self.client.post(reverse('tasks:turno-management'), data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['id_Funcionario'], self.funcionario.pk)
