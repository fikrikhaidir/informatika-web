# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 04:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='berita_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(default='', max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='upload/berita')),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('publish', models.DateField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(default='', max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='gallery_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(default='', max_length=20)),
                ('caption', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(blank=True, default='', upload_to='upload/gallery')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='staff_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(default='', max_length=20)),
                ('nidn', models.CharField(default='', max_length=10)),
                ('jabatan', models.CharField(default='', max_length=30)),
                ('gelar', models.CharField(default='', max_length=30)),
                ('pendidikan1', models.CharField(default='', max_length=30)),
                ('pendidikan2', models.CharField(blank=True, default='', max_length=30)),
                ('pendidikan3', models.CharField(blank=True, default='', max_length=30)),
                ('bidang_keahlian1', models.CharField(default='', max_length=50)),
                ('bidang_keahlian2', models.CharField(blank=True, default='', max_length=50)),
                ('bidang_keahlian3', models.CharField(blank=True, default='', max_length=50)),
                ('foto', models.ImageField(blank=True, default='', upload_to='upload/dosen')),
            ],
        ),
    ]
