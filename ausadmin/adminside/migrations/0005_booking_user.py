# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-09-15 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0004_auto_20180915_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.CharField(default='user1', max_length=30),
        ),
    ]
