# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-04 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0021_auto_20200604_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensebasedtransaction',
            name='total_cost',
            field=models.CommaSeparatedIntegerField(default='', max_length=200, null=True),
        ),
    ]
