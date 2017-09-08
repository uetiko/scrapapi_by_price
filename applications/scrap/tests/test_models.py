import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestMarket(object):

    def test_init(self):
        market = mixer.blend('scrap.Market')
        assert market.pk is 1, 'aquí hay un error'
