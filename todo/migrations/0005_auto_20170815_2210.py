# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 02:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170815_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='create_date',
            field=models.DateField(default=datetime.date(2017, 8, 15), null=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='date due'),
        ),
    ]
