from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


class ViewTestCase(TestCase):

    def test_create_user(self):
        data = {
            'username': 'test_user',
            'email': 'test_user@testuser.com',
            'first_name': 'test_user',
            'last_name': 'test_user',
            'password': 'test_user',
        }

        response = self.client.post(reverse('acconts:cadastrar'), data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(get_user_model().objects.exists())

