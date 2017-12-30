# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 02:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0007_auto_20171128_1824'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='playrecord',
            managers=[
                ('recobjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 18, 32, 30, 818475)),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 28, 18, 32, 30, 818475)),
        ),
    ]