# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-16 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20170814_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='create_date',
            field=models.DateField(verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(verbose_name='date due'),
        ),
    ]
