# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-05 02:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dictionary', '0003_auto_20160105_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name='name')),
                ('address', models.CharField(max_length=512, verbose_name='address')),
                ('phone', models.CharField(max_length=128, verbose_name='phone')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.Region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'shop',
                'verbose_name_plural': 'shops',
                'ordering': ['name'],
            },
        ),
    ]
