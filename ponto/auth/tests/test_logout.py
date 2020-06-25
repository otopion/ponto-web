from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LogoutTest(APITestCase):
    def setUp(self):
        self.url = reverse('auth:logout')
        self.user_class = get_user_model()
        self.active_user = self.user_class.objects.create_user(
            username='user',
            password='password',
            first_name='first_name',
            last_name='last_name',
            email='active@user.com'
        )
        self.client.login(username='user', password='password')

    def tearDown(self):
        self.client.logout()

    def test_get_not_allowed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'].code, 'method_not_allowed')

    def test_failed_logout(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'].code, 'not_authenticated')

    def test_successful_logout(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('detail', response.data)
