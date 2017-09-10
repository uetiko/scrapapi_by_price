from django.test import RequestFactory
from scrap.viewsets import ItemsAPI, ItemSKUAPI, ItemPriceAPI


class TestItems(object):
    _response_items = None
    _response = None

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
        self._response = ItemSKUAPI.as_view()(request, sku=750129930486)
        self._response.render()
        self._returnTupleForResponseItems()
        assert isinstance(self._response.content, bytes), 'error'
        assert self.statusCode200(), 'error in the endpoint'
        assert self.isApplicationJSON()
        assert self.allowGETMethod()

    def test_item_price(self):
        request = RequestFactory().get('/item/price/283.00/')
        self._response = ItemPriceAPI.as_view()(request, price=283.00)
        self._response.render()
        self._returnTupleForResponseItems()
        assert isinstance(self._response.content, bytes), 'error'
        assert self.statusCode200()
        assert self.isApplicationJSON()
        assert self.allowGETMethod()

    def _returnTupleForResponseItems(self):
        self._response_items = list()
        for value in self._response.items():
            self._response_items.append(value)

    def isApplicationJSON(self):
        return 'application/json' in self._response_items[0]

    def allowGETMethod(self):
        return 'GET' in self._response_items[2][1]

    def statusCode200(self):
        """
        :return bool:
        """
        return self._response.status_code is 200
