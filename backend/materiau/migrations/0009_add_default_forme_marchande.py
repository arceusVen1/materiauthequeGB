# -*- coding: utf-8 -*-

"""
Migrations pour ajouter automatique les formes marchandes prédéfinies
"""

from django.db import migrations, models


def add_default_forme_marchande(apps, schema_editor):
    FormeMarchande = apps.get_model('materiau', 'FormeMarchande')
    FormeMarchande.objects.create(type='Vrac')
    FormeMarchande.objects.create(type='Bloc')
    FormeMarchande.objects.create(type='Plaque')
    FormeMarchande.objects.create(type='Profilé')
    FormeMarchande.objects.create(type='Rouleau')

# reverse function si besoin
def remove_default_forme_marchande(apps, schema_editor):
    FormeMarchande = apps.get_model('materiau', 'FormeMarchande')
    FormeMarchande.objects.get(type='Vrac').delete()
    FormeMarchande.objects.get(type='Bloc').delete()
    FormeMarchande.objects.get(type='Plaque').delete()
    FormeMarchande.objects.get(type='Profilé').delete()
    FormeMarchande.objects.get(type='Rouleau').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('materiau', '0008_auto_20170926_1253'),
    ]

    operations = [
        migrations.RunPython(add_default_forme_marchande, remove_default_forme_marchande),
    ]