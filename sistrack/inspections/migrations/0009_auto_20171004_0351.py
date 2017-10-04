# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0008_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inspections.Location'),
        ),
        migrations.AlterField(
            model_name='document',
            name='doc_type',
            field=models.CharField(blank=True, choices=[('c', 'Cause and Effect'), ('d', 'Data Sheet'), ('p', 'P&ID'), ('o', 'other')], default='o', max_length=50),
        ),
    ]