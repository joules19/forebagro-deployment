# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-10 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_remove_expensebasedtransaction_clientele_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expensebasedtransaction',
            name='transaction_type',
        ),
        migrations.AddField(
            model_name='expensebasedtransaction',
            name='eb_client',
            field=models.CharField(choices=[('5', 'Ekedc'), ('9', 'Diesel')], max_length=20, null=True),
        ),
    ]
