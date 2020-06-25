from django.test import TestCase
from django.contrib.auth.models import User

from ..serializers import CadastrarSerializer


class SerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="user-test",
            email="user-test@user.com",
            first_name="user-test",
            last_name="user-test",
            password="user-test"
        )

    def test_cadastro_serializer(self):
        serializer = CadastrarSerializer(self.user)
        data = serializer.data
        self.assertIn('id', data)
        self.assertIn('username', data)
        self.assertIn('email', data)
        self.assertIn('first_name', data)
        self.assertIn('last_name', data)
        self.assertIn('password', data)
