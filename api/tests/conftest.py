import pytest

from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from empresas.models import Empresa


@pytest.fixture
def user():
    return baker.make(User)


@pytest.fixture
def auth(user):
    return baker.make(
        Token,
        user=user
    )


@pytest.fixture
def company():
    return baker.make(Empresa)


@pytest.fixture
def client(user, auth):
    token = Token.objects.get(user__username=user.username)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client
