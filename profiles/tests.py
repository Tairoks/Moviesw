import pytest

from django.test import TestCase, Client
from django.contrib.auth.models import User

client = Client()


class UserTestCase(TestCase):

    @pytest.mark.django_db
    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {
            "username": "test_user",
            "password": "User-13579"
        }
        self.user = User.objects.create_user(self.credentials)

    def test_authentication(self):
        self.client.force_login(self.user)
        response = client.get('/register')
        assert response.status_code == 301 or response.status_code == 302

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout')
        assert response.status_code == 200

# TODO: Check test_logout function
