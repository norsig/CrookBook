# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 03:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20171127_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='case_suspect',
        ),
        migrations.RemoveField(
            model_name='person',
            name='case_victim',
        ),
        migrations.AddField(
            model_name='case',
            name='suspects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suspects', to='cases.Person'),
        ),
        migrations.AddField(
            model_name='case',
            name='victims',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='victims', to='cases.Person'),
        ),
    ]
