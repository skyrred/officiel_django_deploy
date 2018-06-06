# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-06 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180430_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='flags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=120)),
                ('flag_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='match_results',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('match1', models.CharField(max_length=120)),
                ('country1', models.CharField(max_length=120)),
                ('result_1', models.CharField(max_length=120)),
                ('country2', models.CharField(max_length=120)),
                ('match2', models.CharField(max_length=120)),
                ('country3', models.CharField(max_length=120)),
                ('result_2', models.CharField(max_length=120)),
                ('country4', models.CharField(max_length=120)),
                ('match3', models.CharField(max_length=120)),
                ('country5', models.CharField(max_length=120)),
                ('result_3', models.CharField(max_length=120)),
                ('country6', models.CharField(max_length=120)),
                ('match4', models.CharField(max_length=120)),
                ('country7', models.CharField(max_length=120)),
                ('result_4', models.CharField(max_length=120)),
                ('country8', models.CharField(max_length=120)),
                ('match5', models.CharField(max_length=120)),
                ('country9', models.CharField(max_length=120)),
                ('result_5', models.CharField(max_length=120)),
                ('country10', models.CharField(max_length=120)),
            ],
        ),
    ]