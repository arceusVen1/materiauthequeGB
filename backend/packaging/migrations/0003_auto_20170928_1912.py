# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-28 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0002_packaging_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='packaging',
            name='date_de_creation',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='packaging',
            name='materiaux',
            field=models.ManyToManyField(blank=True, to='materiau.MateriauApprouve'),
        ),
    ]
