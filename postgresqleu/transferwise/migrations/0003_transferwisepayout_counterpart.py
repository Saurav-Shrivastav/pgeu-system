# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-31 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferwise', '0002_transferwisepayout'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferwisepayout',
            name='counterpart_account',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='transferwisepayout',
            name='counterpart_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]