# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 02:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0005_auto_20171127_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 18, 26, 50, 781736)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 18, 26, 50, 781736)),
        ),
    ]
