# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-07 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_group_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
