# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-10 12:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170410_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='kurikulum_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(default='', validators=[django.core.validators.MaxValueValidator(9)], verbose_name='Semester')),
                ('makul', models.CharField(default='', max_length=40, verbose_name='Nama Mata Kuliah')),
                ('kode', models.CharField(default='', max_length=5, verbose_name='Kode MK')),
                ('sks', models.PositiveIntegerField(default='', validators=[django.core.validators.MaxValueValidator(9)], verbose_name='SKS')),
            ],
        ),
        migrations.AlterField(
            model_name='staff_model',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, upload_to='upload/dosen', validators=[stdimage.validators.MaxSizeValidator(1028, 768)]),
        ),
    ]