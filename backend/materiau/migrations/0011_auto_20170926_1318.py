# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0010_formemarchande_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiseEnForme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='materiau',
            name='mise_en_forme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiau.MiseEnForme'),
        ),
    ]
