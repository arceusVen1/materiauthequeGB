from django.db import models


class Propriete(models.Model):

    TYPE_CHOICES = (('générale', 'générale'),
                    ("thermique", "thermodynamique"),
                    ('mécanique', 'mécanique'),
                    ('électrique', 'électrique'),
                    ('environnemental', 'environnemental'),
                    )

    class Meta:
        verbose_name = "Propriété"
        verbose_name_plural = "Propriétés"

    nom = models.CharField(max_length=255, unique=True)
    unite = models.CharField(max_length=30, verbose_name='unité', blank=True, null=True)
    definition = models.TextField(verbose_name='définition', default="N.R.")
    type = models.CharField(max_length=255, null=True, blank=True, choices=TYPE_CHOICES)

    @property
    def reference(self):
        return self.nom.lower().replace('\'', '-').replace(' ', '-')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nom = self.nom.title()
        super().save()

    def get_absolute_url(self):
        return u'/propriete/{}'.format(self.reference)

    def __str__(self):
        return self.nom
