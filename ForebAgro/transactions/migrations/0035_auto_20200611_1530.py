# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-11 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0034_auto_20200611_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasetransaction',
            name='clientele_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='salestransaction',
            name='clientele_name',
            field=models.CharField(max_length=100),
        ),
    ]
