# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20160105_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=512, verbose_name='shop name'),
        ),
    ]
