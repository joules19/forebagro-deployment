# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-18 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]