# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatiquement les aspects prédéfinies en cas de destruction de la DB
"""

from django.db import migrations, models


def add_default_propriete(apps, schema_editor):
    Propriete = apps.get_model('materiau', 'Propriete')
    Propriete.objects.create(nom='Masse', unite="kg", type="mécanique")
    Propriete.objects.create(nom='Dureté', unite="N.R.", type="mécanique", definition="Dur/Mou")
    Propriete.objects.create(nom='Rigidité', unite="N.R.", type="mécanique", definition="Rigide/Souple/Elastique")
    Propriete.objects.create(nom='Conductivité électrique', unite="S/m", type="électrique", definition="Oui-Bon/Mauvais/Non")
    Propriete.objects.create(nom='Conductivité thermique', unite="W/m/k", type="thermodynamique", definition="Oui-Bon/Mauvais/Non")
    Propriete.objects.create(nom='Isolation phonique', unite="N.R.", type="mécanique", definition="Oui-Bon/Mauvais/Non")
    Propriete.objects.create(nom='Propriétés magnétiques', unite="N.R.", type="mécanique", definition="Oui-Bon/Mauvais/Non")


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0018_auto_20170926_1439'),
    ]

    operations = [
        migrations.RunPython(add_default_propriete, ),
    ]