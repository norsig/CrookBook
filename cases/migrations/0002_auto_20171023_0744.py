# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='coroner_case_number',
        ),
        migrations.RemoveField(
            model_name='case',
            name='crime_committed',
        ),
        migrations.AddField(
            model_name='event',
            name='coroner_case_number',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='crime_committed',
            field=models.CharField(choices=[('M', 'Murder')], default='M', max_length=1),
        ),
    ]
