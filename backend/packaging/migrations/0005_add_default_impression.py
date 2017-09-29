# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les impression prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_impression(apps, schema_editor):
    Impression = apps.get_model('packaging', 'Impression')
    Impression.objects.create(type='Héliogravure',)
    Impression.objects.create(type='Flexographie',)
    Impression.objects.create(type='Offset',)
    Impression.objects.create(type='Trampographie',)
    Impression.objects.create(type='Autre',)


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0004_auto_20170929_1415'),
    ]

    operations = [
        migrations.RunPython(add_default_impression, ),
    ]