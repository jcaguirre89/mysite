# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-29 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hindsight1', '0056_auto_20171229_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playrecord',
            name='play_rand_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='playrecord',
            name='play_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
