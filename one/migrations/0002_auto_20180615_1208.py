# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-15 06:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='bussiness_values',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='one.List'),
        ),
        migrations.AddField(
            model_name='card',
            name='story_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]