# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sum',
            field=models.FloatField(verbose_name='sum'),
        ),
    ]
