# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 14:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0021_auto_20171209_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 6, 34, 27, 756283)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 6, 34, 27, 756283)),
        ),
    ]