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
    def reference(self):
        return '{}-{}'.format(self.famille, self.numero_de_reference)

    def compute_and_save(self):
        self.numero_de_reference = self.famille.sousfamille_set.count()
        self.save()

    def get_absolute_url(self):
        return u'/materiaux/sous-famille/{}'.format(self.reference)

    def __str__(self):
        return self.reference