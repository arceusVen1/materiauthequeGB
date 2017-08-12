from django.db import models


class Fournisseur(models.Model):

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"

    nom = models.CharField(max_length=255, unique=True, null=True, blank=True)
    site_web = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nom = self.nom.upper()
        super().save()

    def __str__(self):
        return self.nom