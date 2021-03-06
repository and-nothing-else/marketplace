# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('goods', models.PositiveSmallIntegerField(verbose_name='goods count')),
                ('price', models.PositiveSmallIntegerField(help_text='roubles per month', verbose_name='price')),
                ('ordering', models.IntegerField(default=10, verbose_name='ordering')),
                ('is_recommended', models.BooleanField(default=False, verbose_name='is recommended')),
            ],
            options={
                'verbose_name': 'tariff',
                'ordering': ['ordering'],
                'verbose_name_plural': 'tariffs',
            },
        ),
    ]
