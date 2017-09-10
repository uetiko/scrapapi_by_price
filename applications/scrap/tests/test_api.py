import pytest
from django.test import RequestFactory
from scrap.viewsets import ItemsAPI, ItemSKUAPI, ItemPriceAPI
pytestmark = pytest.mark.django_db


class TestItems(object):
    def test_items(self):
        request = RequestFactory().get('/items/')
        response = ItemsAPI.as_view()(request)
        assert response.status_code is 200, 'no paso el test'

    def test_items_content(self):
        request = RequestFactory().get('/items/')
        response = ItemsAPI.as_view()(request)
        response.render()
        assert isinstance(response.content, bytes), 'error'
        assert response.charset == 'utf-8', 'charset error'

    def test_sku_content(self):
        request = RequestFactory().get('/items/750129930486/')
        response = ItemSKUAPI.as_view()(request, sku=750129930486)
        response.render()
        assert isinstance(response.content, bytes), 'error'
        assert response.status_code is 200, 'error in the endpoint'

    def test_item_price(self):
        request = RequestFactory().get('/item/price/283.00/')
        response = ItemPriceAPI.as_view()(request, price=283.00)
        response.render()
        assert isinstance(response.content, bytes), 'error'
        assert response.status_code is 200
