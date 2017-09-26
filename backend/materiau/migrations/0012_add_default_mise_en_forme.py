# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les mise en formes prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_forme_marchande(apps, schema_editor):
    MiseEnForme = apps.get_model('materiau', 'MiseEnForme')
    MiseEnForme.objects.create(type='Usinage')
    MiseEnForme.objects.create(type='Découpage')
    MiseEnForme.objects.create(type='Déformation')
    MiseEnForme.objects.create(type='Moulage')
    MiseEnForme.objects.create(type='Modelage manuel')
    MiseEnForme.objects.create(type='Autre')


# reverse function si besoin
def remove_default_forme_marchande(apps, schema_editor):
    MiseEnForme = apps.get_model('materiau', 'MiseEnForme')
    MiseEnForme.objects.get(type='Usinage').delete()
    MiseEnForme.objects.get(type='Découpage').delete()
    MiseEnForme.objects.get(type='Déformation').delete()
    MiseEnForme.objects.get(type='Moulage').delete()
    MiseEnForme.objects.get(type='Modelage manuel').delete()
    MiseEnForme.objects.get(type='Autre').delete()



class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0011_auto_20170926_1318'),
    ]

    operations = [
        migrations.RunPython(add_default_forme_marchande, remove_default_forme_marchande),
    ]