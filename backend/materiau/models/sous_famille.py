from django.db import models
from .famille import Famille


class SousFamille(models.Model):

    class Meta:
        verbose_name = "Sous famille"
        verbose_name_plural = "Sous Familles"

    matiere = models.CharField(max_length=255, null=True, blank=True)
    numero_de_reference = models.IntegerField(null=True, blank=True)
    famille = models.ForeignKey(Famille)

    @property
    def nombre_de_materiaux(self):
        return self.materiau_set.count()

    @property
    def reference(self):
        return '{}-{}'.format(self.famille.reference, self.numero_de_reference)

    def save(self, *args, **kwargs):
        if self.numero_de_reference is None:
            try:
                self.numero_de_reference = self.famille.sousfamille_set.last().numero_de_reference + 1
            except AttributeError:
                self.numero_de_reference = 0
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return u'/materiaux/sous-famille/{}'.format(self.reference)

    def __str__(self):
        return '{} - {}'.format(self.reference, self.matiere)