# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-16 19:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0030_auto_20171216_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 11, 14, 33, 371291)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 16, 11, 14, 33, 371291)),
        ),
    ]
