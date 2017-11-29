# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0013_auto_20171127_0518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='suspects',
            field=models.ManyToManyField(blank=True, related_name='suspects1', to='cases.Person'),
        ),
        migrations.AlterField(
            model_name='case',
            name='victims',
            field=models.ManyToManyField(blank=True, related_name='victims1', to='cases.Person'),
        ),
    ]