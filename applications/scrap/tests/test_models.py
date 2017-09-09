from mixer.backend.django import mixer


class TestMarket(object):
    def test_init(self):
        market = mixer.blend('scrap.Market', name='chedraui')
        assert market.pk is 1, 'aquí hay un error'

    def test_new_Market(self):
        market = mixer.blend('scrap.Market', name='San Pablo')
        assert market.name is 'San Pablo'
