# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_skyfoot_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='skyfoot_cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='skyfoot_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='skyfoot_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('url', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.skyfoot_cat')),
            ],
        ),
        migrations.AddField(
            model_name='skyfoot_comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.skyfoot_post'),
        ),
    ]