# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 06:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upc', models.CharField(max_length=20, verbose_name='upc/sku')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('product_page', models.CharField(max_length=140, verbose_name='pagina de producto')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='precio')),
                ('image', models.URLField(max_length=150, verbose_name='imagen')),
                ('description', models.CharField(max_length=140, verbose_name='descripcion')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='tienda')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='lugar')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_market', related_query_name='relationship_market', to='scrap.Market', verbose_name='tienda')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationship_place', related_query_name='relationship_place', to='scrap.Place', verbose_name='Lugar'),
        ),
    ]
