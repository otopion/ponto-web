from django.test import TestCase
from django.contrib.auth import get_user_model
from ponto.auth.serializers import UserSerializer


class SerializerTestCase(TestCase):
    def test_user_serializer(self):
        serializer = UserSerializer()
        self.assertIn('username', serializer.fields)
        self.assertIn('password', serializer.fields)
        self.assertIn('first_name', serializer.fields)
        self.assertIn('last_name', serializer.fields)
        self.assertIn('email', serializer.fields)

    def test_should_have_instance_user(self):
        self.assertEqual(get_user_model(), UserSerializer.Meta.model)
