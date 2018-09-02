# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-02 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('catname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='adminside/static/itemimages')),
                ('price', models.IntegerField(blank=True)),
                ('categorychosen', models.CharField(blank=True, max_length=40)),
                ('no2', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('adhar', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('emailid', models.TextField(max_length=30)),
            ],
        ),
    ]
