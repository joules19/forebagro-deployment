# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-12 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0039_auto_20200612_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionrecord',
            name='clientele_id',
            field=models.IntegerField(null=True),
        ),
    ]
