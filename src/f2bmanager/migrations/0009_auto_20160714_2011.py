# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f2bmanager', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='customaction',
            name='ip_port',
            field=models.CharField(blank=True, default='ssh', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customaction',
            name='ip_protocol',
            field=models.CharField(blank=True, choices=[('tcp', 'TCP'), ('udp', 'UDP'), ('icmp', 'ICMP'), ('all', 'ALL')], default='tcp', max_length=10, null=True),
        ),
    ]