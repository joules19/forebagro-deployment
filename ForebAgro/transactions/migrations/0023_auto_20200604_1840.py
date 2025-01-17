# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-04 18:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0022_auto_20200604_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensebasedtransaction',
            name='total_cost',
            field=models.CharField(default='', max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
