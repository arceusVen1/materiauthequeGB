# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0022_materiau_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formemarchande',
            options={'verbose_name': 'Forme marchande', 'verbose_name_plural': 'Formes Marchandes'},
        ),
        migrations.AlterModelOptions(
            name='miseenforme',
            options={'verbose_name': 'Mise en forme', 'verbose_name_plural': 'Mises en Forme'},
        ),
    ]
