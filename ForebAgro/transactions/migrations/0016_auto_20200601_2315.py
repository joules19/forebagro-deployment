# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-01 23:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_auto_20200601_2310'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='expensebasedtransaction',
            table='expense_based_transaction',
        ),
    ]
