# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20170413_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_model',
            name='gelar2',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Gelar Pendidikan S2'),
        ),
        migrations.AlterField(
            model_name='staff_model',
            name='gelar3',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='Gelar Pendidikan S3'),
        ),
    ]