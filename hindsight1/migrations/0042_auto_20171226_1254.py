# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 20:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0041_auto_20171226_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 12, 54, 46, 679909)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 12, 54, 46, 679909)),
        ),
    ]
