# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-11 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f2bmanager', '0004_auto_20160711_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]