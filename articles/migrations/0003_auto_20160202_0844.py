# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 05:44
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160202_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='browser_title',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='browser title'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='meta description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(help_text='550x300px', upload_to='articles', verbose_name='image'),
        ),
    ]
