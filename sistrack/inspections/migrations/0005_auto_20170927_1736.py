# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0004_testinstance_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinstance',
            name='comments',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
