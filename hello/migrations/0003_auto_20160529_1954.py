# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20160529_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='likecount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='viewcount',
            field=models.IntegerField(default=0),
        ),
    ]