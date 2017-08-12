# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0003_auto_20170811_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('site_web', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Fournisseur',
                'verbose_name_plural': 'Fournisseurs',
            },
        ),
        migrations.AlterModelOptions(
            name='materiau',
            options={'verbose_name': 'Matériau', 'verbose_name_plural': 'Matériaux'},
        ),
        migrations.AddField(
            model_name='materiau',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiau.Fournisseur'),
        ),
    ]
