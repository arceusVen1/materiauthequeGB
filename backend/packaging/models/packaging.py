from django.db import models
from materiau.models import Materiau


class Packaging(models.Model):

    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    nom_produit = models.CharField(verbose_name="Nom du produit", blank=True)
    materiaux = models.ManyToManyField(Materiau, blank=True)
    fabrication = models.TextField(verbose_name="Procédé de fabrication", blank=True, null=True)
    mise_en_forme = models.TextField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='packaging', null=True, blank=True)




