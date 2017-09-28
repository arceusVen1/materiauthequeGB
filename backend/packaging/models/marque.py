from django.db import models


class Marque(models.Model):

    nom = models.CharField(max_length=255, unique=True)
    site_web = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.nom = self.nom.upper()
        super().save(*args, **kwargs)