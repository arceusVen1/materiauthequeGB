# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les traitements prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_traitement(apps, schema_editor):
    Traitement = apps.get_model('materiau', 'Traitement')
    Traitement.objects.create(type='Peinture')
    Traitement.objects.create(type='Traitement de surface')
    Traitement.objects.create(type='Recouvrement')
    Traitement.objects.create(type='Impression')
    Traitement.objects.create(type='Autre')


# reverse function si besoin
def remove_default_traitement(apps, schema_editor):
    Traitement = apps.get_model('materiau', 'Traitement')
    Traitement.objects.get(type='Peinture').delete()
    Traitement.objects.get(type='Traitement de surface').delete()
    Traitement.objects.get(type='Recouvrement').delete()
    Traitement.objects.get(type='Impression').delete()
    Traitement.objects.get(type='Autre').delete()



class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0013_traitement'),
    ]

    operations = [
        migrations.RunPython(add_default_traitement, remove_default_traitement),
    ]