# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-15 16:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0003_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('eventname', models.CharField(max_length=30)),
                ('c1', models.CharField(max_length=30)),
                ('c2', models.CharField(max_length=30)),
                ('c3', models.CharField(max_length=30)),
                ('c4', models.CharField(max_length=30)),
                ('c5', models.CharField(max_length=30)),
                ('c6', models.CharField(max_length=30)),
                ('totalcost', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='adminside/static/images/play.png', upload_to='adminside/static/itemimages'),
        ),
    ]
