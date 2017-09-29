# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les finitions prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_finition(apps, schema_editor):
    Finition = apps.get_model('packaging', 'Finition')
    Finition.objects.create(type='Vernis',)
    Finition.objects.create(type='Vernis sélectif',)
    Finition.objects.create(type='Pelliculage',)
    Finition.objects.create(type='Dorure',)
    Finition.objects.create(type='Gaufrage',)
    Finition.objects.create(type='Découpe',)
    Finition.objects.create(type='Autre',)


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0006_finition'),
    ]

    operations = [
        migrations.RunPython(add_default_finition, ),
    ]