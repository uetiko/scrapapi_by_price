import pytest
import django
from django.conf import settings

pytestmark = pytest.mark.django_db


@pytest.fixture(autouse=True)
def enable_db_access_for_all_test(db):
    pass


def pytest_configure():
    settings.DEBUG = False
    django.setup()


@pytest.fixture
def db_doctest(request, _django_cursor_wrapper):
    from django.test import TestCase as django_case
    _django_cursor_wrapper.enable()
    request.addfinalizer(_django_cursor_wrapper.disable)
    case = django_case(methodName='__init__')
    case._pre_setup()
    request.addfinalizer(case._post_teardown)


@pytest.fixture()
def real_db(_django_cursor_wrapper):
        _django_cursor_wrapper.enable()
