# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-17 01:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0031_auto_20171216_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 17, 24, 34, 399932)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 17, 24, 34, 399932)),
        ),
    ]
