from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status


class LastUsertTestCase(TestCase):

    def _create_user(self):
        data = {
            'username': 'test_userr',
            'email': 'test_user@testuser.com',
            'first_name': 'test_user',
            'last_name': 'test_user',
            'password': 'test_user',
        }

        response = self.client.post(reverse('acconts:cadastrar'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_last_user(self):
        self._create_user()
        user = get_user_model().objects.get(username='test_userr')
        response = self.client.get(reverse('auth:last_user'))

        self.assertEqual(response.data['username'], user.username)

        self.assertContains(response, user)
