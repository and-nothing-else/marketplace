# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-12 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0004_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=16, verbose_name='value')),
                ('description', models.TextField(blank=True, help_text='html tags allowed', verbose_name='description')),
            ],
            options={
                'verbose_name': 'size',
                'ordering': ['value'],
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='SizeSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
            options={
                'verbose_name': 'size set',
                'ordering': ['name'],
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.AddField(
            model_name='size',
            name='size_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dictionary.SizeSet', verbose_name='size set'),
        ),
    ]
