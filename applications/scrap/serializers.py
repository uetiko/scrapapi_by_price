from rest_framework import serializers
from scrap.models import Market
from scrap.models import Place
from scrap.models import Item


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ('name',)


class PlaceSerializer(serializers.ModelSerializer):
    market = MarketSerializer(many=True, read_only=True)
    class Meta:
        model = Place
        fields = ('market', 'name')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = (
            'upc', 'name', 'product_page',
            'price', 'image', 'description',
        )
