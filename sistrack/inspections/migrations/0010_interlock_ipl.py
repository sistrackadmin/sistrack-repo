# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0009_auto_20171004_0351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interlock_number', models.CharField(max_length=50)),
                ('interlock_description', models.CharField(blank=True, max_length=300, null=True)),
                ('interlock_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.Location')),
            ],
            options={
                'ordering': ['interlock_number'],
            },
        ),
        migrations.CreateModel(
            name='Ipl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initiator', models.CharField(max_length=50)),
                ('ipl_description', models.CharField(max_length=300)),
                ('ipl_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inspections.Location')),
            ],
            options={
                'ordering': ['ipl_unit'],
            },
        ),
    ]
