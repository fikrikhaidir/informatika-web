# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-15 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20170415_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokumen_model',
            name='deskripsi',
            field=models.CharField(default='', max_length=100, verbose_name='Nama Dokumen'),
        ),
        migrations.AlterField(
            model_name='dokumen_model',
            name='file',
            field=models.FileField(blank=True, upload_to='upload/document', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='dokumen_model',
            name='keterangan',
            field=models.CharField(default='', max_length=50, verbose_name='Deskripsi'),
        ),
    ]