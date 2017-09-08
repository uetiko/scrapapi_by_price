from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Market(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name='tienda'
    )


class Place(models.Model):
    market = models.ForeignKey(
        Market,
        verbose_name="tienda",
        related_name="relationship_market",
        related_query_name="relationship_market",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=15,
        verbose_name='lugar'
    )

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"

    def __str__(self):
        return super(self.__class__, self).__str__()


class Item(models.Model):
    place = models.ForeignKey(
        Place,
        verbose_name="Lugar",
        related_name="relationship_place",
        related_query_name="relationship_place",
        on_delete=models.CASCADE
    )
    upc = models.CharField(
        max_length=20,
        verbose_name='upc/sku'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Nombre del producto'
    )
    product_page = models.CharField(
        max_length=140,
        verbose_name='pagina de producto'
    )
    price = models.DecimalField(
        verbose_name='precio',
        max_digits=5,
        decimal_places=2
    )
    image = models.URLField(
        verbose_name="imagen",
        max_length=150,
        blank=False,
        null=False,
    )
    description = models.CharField(
        verbose_name="descripcion",
        max_length=140,
        blank=False,
        null=False
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return super(self.__class__, self).__str__()
