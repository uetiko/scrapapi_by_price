from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrap.serializers import ItemSerializer
from scrap.models import Item


class ItemsAPI(APIView):
    def get(self, request):
        return ItemSerializer(
            Item.objects.all(), status.HTTP_200_OK
        )


class ItemSKUAPI(APIView):
    def get(self, request, sku):
        return ItemSerializer(
            Item.objects.filter(upc=sku), status.HTTP_200_OK
        )


class ItemPriceAPI(APIView):
    def get(self, request, price):
        return ItemSerializer(
            Item.objects.filter(price=price), status.HTTP_200_OK
        )
