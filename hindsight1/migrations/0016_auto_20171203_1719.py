# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 01:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0015_auto_20171203_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 3, 17, 19, 42, 276793)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 3, 17, 19, 42, 276793)),
        ),
    ]
