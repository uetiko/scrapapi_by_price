import sys
from django.core.management.base import BaseCommand
from scrap.helpers import ScrapHelper
from scrap.models import Market
from scrap.models import Place
from scrap.models import Item


class Command(BaseCommand):

    """Docstring for command. """

    def handle(self, *args, **kwargs):
        self.stdout.write("creando productos")
        helper = ScrapHelper()
        market, create_market = Market.objects.get_or_create(name='chedraui')
        place, create_place = Place.objects.get_or_create(
            market=market, name='Ajusco'
        )
        url = 'https://www.chedraui.com.mx'
        count = 0
        for item in helper.getItems():
            product, create = Item.objects.get_or_create(
                place=place,
                upc=item.get('P_sku_id')[0],
                name=item.get('P_name')[0],
                product_page="{}/{}".format(
                    url,
                    item.get('P_product_page_url')[0]
                ),
                price=item.get('P_price')[0],
                image="{}{}".format(
                    url,
                    item.get('P_small_image_url')[0]
                ),
                description=item.get('P_short_desc')[0]
            )
            if create:
                count += 1

        self.stdout.write("total de items creados: {}".format(str(count)))
