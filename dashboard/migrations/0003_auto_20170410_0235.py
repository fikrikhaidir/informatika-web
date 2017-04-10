# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-10 02:35
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170410_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_model',
            name='foto',
            field=stdimage.models.StdImageField(upload_to='upload/dosen', validators=[stdimage.validators.MaxSizeValidator(1028, 768)]),
        ),
    ]
