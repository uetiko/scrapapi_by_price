from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrap.serializers import ItemSerializer
from scrap.models import Item


class ItemsAPI(APIView):
    def get(self, request):
        return Response(
            ItemSerializer(
                Item.objects.all(), many=True
            ).data, status=status.HTTP_200_OK
        )


class ItemSKUAPI(APIView):
    def get(self, request, sku):
        return Response(ItemSerializer(
            Item.objects.filter(upc=sku), many=True).data,
            status=status.HTTP_200_OK
        )


class ItemPriceAPI(APIView):
    def get(self, request, price):
        return Response(ItemSerializer(
            Item.objects.filter(price=float(price)), many=True).data,
            status=status.HTTP_200_OK
        )
