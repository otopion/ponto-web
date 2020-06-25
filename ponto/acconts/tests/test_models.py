from django.test import TestCase

from django.contrib.auth.models import User


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            username="user-test",
            email="user-test@user.com",
            first_name="user-test",
            last_name="user-test",
            password="user-test"
        )

    def test_user_exist(self):
        self.assertTrue(User.objects.exists())




