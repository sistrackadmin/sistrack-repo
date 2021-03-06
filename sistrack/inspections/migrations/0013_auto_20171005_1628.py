# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0012_auto_20171005_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipl',
            name='input_elements',
            field=models.ManyToManyField(blank=True, related_name='_ipl_input_elements_+', related_query_name='IPL input elements', to='inspections.Device'),
        ),
        migrations.AlterField(
            model_name='ipl',
            name='output_elements',
            field=models.ManyToManyField(blank=True, related_name='_ipl_output_elements_+', related_query_name='IPL output elements', to='inspections.Device'),
        ),
    ]
