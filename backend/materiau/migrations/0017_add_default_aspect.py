# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les aspects prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_aspect(apps, schema_editor):
    Aspect = apps.get_model('materiau', 'Aspect')
    Aspect.objects.create(type='Visuel', qualificatif="Opaque")
    Aspect.objects.create(type='Visuel', qualificatif="Translucide")
    Aspect.objects.create(type='Visuel', qualificatif="Opalescent")
    Aspect.objects.create(type='Visuel', qualificatif="Diffusant")
    Aspect.objects.create(type='Visuel', qualificatif="Dépoli")
    Aspect.objects.create(type='Visuel', qualificatif="Brossé")
    Aspect.objects.create(type='Visuel', qualificatif="Transparent")
    Aspect.objects.create(type='Visuel', qualificatif="Brillant")
    Aspect.objects.create(type='Visuel', qualificatif="Satiné")
    Aspect.objects.create(type='Visuel', qualificatif="Mat")
    Aspect.objects.create(type='Visuel', qualificatif="Texturé")
    Aspect.objects.create(type='Visuel', qualificatif="Réfléchissant")
    Aspect.objects.create(type='Visuel', qualificatif="Illusion")
    Aspect.objects.create(type='Visuel', qualificatif="Autre")
    Aspect.objects.create(type='Tactile', qualificatif="Lisse")
    Aspect.objects.create(type='Tactile', qualificatif="Rugueux")
    Aspect.objects.create(type='Tactile', qualificatif="Soyeux")
    Aspect.objects.create(type='Tactile', qualificatif="Duveteux")
    Aspect.objects.create(type='Tactile', qualificatif="Pelucheux")
    Aspect.objects.create(type='Tactile', qualificatif="Doux")
    Aspect.objects.create(type='Tactile', qualificatif="Gommé")
    Aspect.objects.create(type='Tactile', qualificatif="Fluide")
    Aspect.objects.create(type='Tactile', qualificatif="Texturé")
    Aspect.objects.create(type='Tactile', qualificatif="Chaud")
    Aspect.objects.create(type='Tactile', qualificatif="Froid")
    Aspect.objects.create(type='Tactile', qualificatif="Réponse au contact")
    Aspect.objects.create(type='Tactile', qualificatif="Autre")


# reverse function si besoin
def remove_default_traitement(apps, schema_editor):
    Aspect = apps.get_model('materiau', 'Aspect')
    Aspect.objects.get(type='Peinture').delete()
    Aspect.objects.get(type='Aspect de surface').delete()
    Aspect.objects.get(type='Recouvrement').delete()
    Aspect.objects.get(type='Impression').delete()
    Aspect.objects.get(type='Autre').delete()



class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0016_auto_20170926_1408'),
    ]

    operations = [
        migrations.RunPython(add_default_aspect,),
    ]