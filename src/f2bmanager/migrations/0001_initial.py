# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-01 23:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_name', models.CharField(max_length=20, unique=True)),
                ('action_desc', models.CharField(blank=True, max_length=500)),
                ('action_data', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultJail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ignoreip', models.CharField(blank=True, default='127.0.0.1/8', max_length=500)),
                ('bantime', models.IntegerField(default=600)),
                ('findtime', models.IntegerField(default=600)),
                ('maxretry', models.IntegerField(default=3)),
                ('backend', models.CharField(choices=[('auto', 'Auto'), ('pyinotify', 'Pyinotify'), ('gamin', 'Gamin'), ('polling', 'Polling')], default='auto', max_length=15)),
                ('usedns', models.CharField(choices=[('warn', 'Warn'), ('yes', 'Yes'), ('no', 'No')], default='warn', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_name', models.CharField(max_length=20, unique=True)),
                ('filter_desc', models.CharField(blank=True, max_length=500)),
                ('filter_data', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ignoreip', models.CharField(blank=True, default='127.0.0.1/8', max_length=500)),
                ('bantime', models.IntegerField(default=600)),
                ('findtime', models.IntegerField(default=600)),
                ('maxretry', models.IntegerField(default=3)),
                ('backend', models.CharField(choices=[('auto', 'Auto'), ('pyinotify', 'Pyinotify'), ('gamin', 'Gamin'), ('polling', 'Polling')], default='auto', max_length=15)),
                ('usedns', models.CharField(choices=[('warn', 'Warn'), ('yes', 'Yes'), ('no', 'No')], default='warn', max_length=5)),
                ('jail_name', models.CharField(max_length=20, unique=True)),
                ('jail_desc', models.CharField(blank=True, max_length=500)),
                ('jail_data', models.CharField(blank=True, max_length=1000)),
                ('jail_actionvars', models.CharField(blank=True, max_length=200)),
                ('logpath', models.CharField(max_length=300)),
                ('enabled', models.CharField(choices=[('true', 'True'), ('false', 'False')], default='true', max_length=6)),
                ('jail_action', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='f2bmanager.Action')),
                ('jail_filter', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='f2bmanager.Filter')),
            ],
        ),
    ]
