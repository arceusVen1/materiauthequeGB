from django.db import models
from .propriete import Propriete
from .materiau import Materiau


class Attribut(models.Model):

    class Meta:
        verbose_name = "Attribut"
        verbose_name_plural = "Attributs"

    materiau = models.ForeignKey(Materiau, verbose_name='matériau')
    propriete = models.ForeignKey(Propriete, verbose_name='propriété', blank=True)
    valeur = models.FloatField(null=True, blank=True)
    qualificatif = models.CharField(max_length=255, blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.qualificatif is not None:

            # Pour mettre le qualificatif dans un format correct

            liste = self.qualificatif.split(' ')
            liste[0] = liste[0].title()
            self.qualificatif = ' '.join(liste)
        super().save()

    def __str__(self):
        return self.propriete.nom