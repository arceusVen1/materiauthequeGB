# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0014_add_default_traitement'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiau',
            name='traitement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiau.Traitement'),
        ),
    ]
