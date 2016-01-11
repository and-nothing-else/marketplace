# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'catalog sections',
                'verbose_name': 'catalog section',
            },
        ),
    ]
