from django.db import models


class Famille(models.Model):

    class Meta:
        verbose_name = "Famille"
        verbose_name_plural = "Familles"

    matiere = models.CharField(max_length=255, blank=True, null=True)

    # l'url de l'API utilise ce champs comme slug (voir lookup_field)
    reference = models.CharField(max_length=2, unique=True, blank=True, null=True)

    def compute_and_save(self):
        self.matiere = self.matiere.upper()
        self.reference = self.reference.upper()
        self.save()

    def get_absolute_url(self):
        return u'/materiaux/famille/{}'.format(self.reference)

    def __str__(self):
        return '{} - {}'.format(self.reference, self.matiere)
