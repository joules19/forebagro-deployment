# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-18 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_purchasetransaction_salestransaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salestransaction',
            old_name='Docket_number',
            new_name='docket_number',
        ),
    ]