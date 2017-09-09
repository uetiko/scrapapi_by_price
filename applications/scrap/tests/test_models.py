from mixer.backend.django import mixer
from scrap.models import Item
from scrap.models import Place


class TestMarket(object):
    def test_init(self):
        market = mixer.blend('scrap.Market', name='chedraui')
        assert isinstance(market.pk, int), 'aquí hay un error'

    def test_new_Market(self):
        market = mixer.blend('scrap.Market', name='San Pablo')
        assert market.name is 'San Pablo'

    def test_count_items(self):
        items = Item.objects.count()
        assert items is 24, 'error'

    def test_count_places(self):
        place = Place.objects.count()
        assert place is 1, 'error'
