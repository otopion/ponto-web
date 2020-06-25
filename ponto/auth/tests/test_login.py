from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoginTestCase(APITestCase):
    def setUp(self):
        self.url_login = reverse('auth:login')
        self.url_user = reverse('auth:user_details')
        self.user_class = get_user_model()

    def _post_login(self, data):
        return self.client.post(self.url_login, data, format='json')

    def _test_wrong_username(self, username, code):
        data = {
            'password': 'nada'
        }
        if username is not None:
            data['username'] = username
        response = self._post_login(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertEqual(code, response.data['username'][0].code)

    def test_required_username(self):
        self._test_wrong_username(None, 'required')

    def test_empty_username(self):
        self._test_wrong_username('', 'blank')

    def test_max_length_username(self):
        self._test_wrong_username('a' * 101, 'max_length')

    def test_min_length_username(self):
        self._test_wrong_username('a' * 3, 'min_length')

    def _test_wrong_password(self, password, code):
        data = {
            'username': 'nada'
        }
        if password is not None:
            data['password'] = password
        response = self._post_login(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password', response.data)
        self.assertEqual(code, response.data['password'][0].code)

    def test_required_password(self):
        self._test_wrong_password(None, 'required')

    def test_blank_password(self):
        self._test_wrong_password('', 'blank')

    def test_wrong_credentials(self):
        response = self._post_login({
            'username': 'aaaa',
            'password': 'bbb'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual('invalid', response.data['non_field_errors'][0].code)

    def test_inactive_user(self):
        self.user_class.objects.create_user(
            username='abcde',
            password='abcde',
            is_active=False
        )
        response = self._post_login({
            'username': 'abcde',
            'password': 'abcde'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual('invalid', response.data['non_field_errors'][0].code)

    def test_successful_login(self):
        user = self.user_class.objects.create_user(
            username='user',
            password='password',
            first_name='first_name',
            last_name='last_name',
            email='email@mail.com'
        )
        response = self._post_login({
            'username': 'user',
            'password': 'password'
        })
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        response = self.client.get(self.url_user)
        with self.subTest():
            self.assertContains(response, user.username)
            self.assertContains(response, user.first_name)
            self.assertContains(response, user.last_name)
            self.assertContains(response, user.email)

    def _test_remember_me(self, remember_me):
        self.user_class.objects.create_user(
            username='user',
            password='password',
            first_name='first_name',
            last_name='last_name',
            email='email@mail.com'
        )
        response = self._post_login({
            'username': 'user',
            'password': 'password',
            'remember_me': remember_me
        })
        self.assertTrue(settings.SESSION_COOKIE_NAME in response.cookies)
        self.assertIn('expires', response.cookies[settings.SESSION_COOKIE_NAME])
        if remember_me:
            self.assertNotEqual('', response.cookies[settings.SESSION_COOKIE_NAME]['expires'])
        else:
            self.assertEqual('', response.cookies[settings.SESSION_COOKIE_NAME]['expires'])

    def test_remember_me_checked(self):
        self._test_remember_me(True)

    def test_remember_me_unchecked(self):
        self._test_remember_me(False)
