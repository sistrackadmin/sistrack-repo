# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0003_auto_20170927_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='testinstance',
            name='comments',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
