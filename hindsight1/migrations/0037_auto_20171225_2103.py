# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 05:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0036_auto_20171225_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 25, 21, 3, 11, 89342)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 25, 21, 3, 11, 89342)),
        ),
    ]
