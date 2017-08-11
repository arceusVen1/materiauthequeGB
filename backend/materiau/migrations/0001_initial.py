# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.CharField(blank=True, max_length=2, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Famille',
                'verbose_name_plural': 'Familles',
            },
        ),
        migrations.CreateModel(
            name='Materiau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('usage', models.TextField(default='N.R.')),
                ('date_de_creation', models.DateField(auto_now_add=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='materiaux')),
            ],
            options={
                'verbose_name': 'Materiau',
                'verbose_name_plural': 'Materiaux',
            },
        ),
        migrations.CreateModel(
            name='SousFamille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matiere', models.CharField(max_length=255)),
                ('numero_de_reference', models.IntegerField(blank=True, null=True)),
                ('famille', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiau.Famille')),
            ],
            options={
                'verbose_name': 'Sous famille',
                'verbose_name_plural': 'Familles',
            },
        ),
        migrations.AddField(
            model_name='materiau',
            name='sous_famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiau.SousFamille'),
        ),
    ]
