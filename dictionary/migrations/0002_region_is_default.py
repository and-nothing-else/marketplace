# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]
