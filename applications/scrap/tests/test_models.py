from mixer.backend.django import mixer
from scrap.models import Item
from scrap.models import Place


class TestMarket(object):

    def test_init(self):
        market = mixer.blend('scrap.Market', name='chedraui')
        assert isinstance(market.pk, int), 'aquí hay un error'

    def test_count_items(self):
        items = Item.objects.count()
        assert items >= 24, 'error'

    def test_count_places(self):
        place = Place.objects.count()
        assert place > 0, 'error'

    def test_relationship(self):
        place = Place.objects.get(name='Ajusco')
        items = Item.objects.filter(place=place)
        assert len(items) > 0, 'error'
