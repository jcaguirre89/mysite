# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 21:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0049_auto_20171226_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 13, 22, 4, 200343)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 13, 22, 4, 200343)),
        ),
    ]
