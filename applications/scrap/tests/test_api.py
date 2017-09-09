import pytest
from django.test import RequestFactory
from scrap.viewsets import ItemsAPI, ItemSKUAPI, ItemPriceAPI
pytestmark = pytest.mark.django_db


class TestItems(object):
    def test_items(self):
        request = RequestFactory().get('/items/')
        response = ItemsAPI.as_view()(request)
        assert response.status_code is 200, 'no paso el test'
