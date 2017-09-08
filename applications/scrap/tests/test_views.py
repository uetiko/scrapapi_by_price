import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from mixer.backend.django import mixer
from scrap.views import HomeView
from scrap.views import AdminView

pytestmark = pytest.mark.django_db


class TestHomeView(object):
    def test_anonymous(self):
        request = RequestFactory().get('/')
        response = HomeView.as_view()(request)
        assert response.status_code is 200, 'you need code home page'


class TestAdminView(object):
    def test_anonymous(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        response = AdminView.as_view()(request)
        assert 'login' in response.url

    def test_superuser(self):
        request = RequestFactory().get('/')
        request.user = mixer.blend('auth.User', is_superuser=True)
        response = AdminView.as_view()(request)
        assert response.status_code is 200, 'debe ser superuser'
