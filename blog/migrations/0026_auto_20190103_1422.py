# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_tokens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokens',
            name='token',
            field=models.CharField(default=None, max_length=2000),
        ),
    ]