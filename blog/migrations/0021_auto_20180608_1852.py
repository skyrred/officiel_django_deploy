# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-08 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_group_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirts',
            name='description',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='shirts',
            name='num_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='shirts',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='shirts',
            name='title',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]
