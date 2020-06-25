from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserDetailsTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('auth:user_details')
        self.user_class = get_user_model()
        self.active_user = self.user_class.objects.create_user(
            username='active_user',
            password='active_user',
            first_name='active_first_name',
            last_name='active_last_name',
            email='active@user.com',
        )
        self.non_active_user = self.user_class.objects.create_user(
            username='non_active_user',
            password='non_active_user',
            first_name='non_active_first_name',
            last_name='non_active_last_name',
            email='non_active@user.com',
            is_active=False
        )

    def tearDown(self):
        self.client.logout()

    def test_active_user(self):
        self.client.login(username='active_user', password='active_user')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.active_user.username)
        self.assertContains(response, self.active_user.first_name)
        self.assertContains(response, self.active_user.last_name)
        self.assertContains(response, self.active_user.email)

    def test_non_active_user(self):
        self.client.login(username='non_active_user', password='non_active_user')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'].code, 'not_authenticated')

    def test_non_logged_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'].code, 'not_authenticated')