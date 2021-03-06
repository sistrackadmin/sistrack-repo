# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0010_interlock_ipl'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipl',
            name='ipl_components',
            field=models.ManyToManyField(to='inspections.Device', verbose_name='IPL components'),
        ),
        migrations.AddField(
            model_name='ipl',
            name='ipl_doc_references',
            field=models.ManyToManyField(to='inspections.Document', verbose_name='IPL reference documents'),
        ),
        migrations.AddField(
            model_name='ipl',
            name='ipl_interlock_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.Interlock'),
        ),
    ]
