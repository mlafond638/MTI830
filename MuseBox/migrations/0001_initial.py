# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('artistLocation', models.CharField(max_length=100, null=True)),
                ('artistName', models.CharField(max_length=100, null=True)),
                ('duration', models.DecimalField(decimal_places=3, max_digits=20, null=True)),
                ('popularity', models.CharField(max_length=100, null=True)),
                ('year', models.IntegerField(null=True)),
                ('artistFamiliarity', models.DecimalField(decimal_places=1, max_digits=20, null=True)),
                ('artistPopularity', models.DecimalField(decimal_places=1, max_digits=20, null=True)),
                ('gender1', models.CharField(max_length=100, null=True)),
                ('gender2', models.CharField(max_length=100, null=True)),
                ('gender3', models.CharField(max_length=100, null=True)),
                ('gender4', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
