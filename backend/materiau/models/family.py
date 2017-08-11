from django.db import models


class Family(models.Model):

    constituent = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=2, unique=True, blank=True, null=True)

    def compute_and_save(self):
        self.reference = self.reference.upper()
        self.save()

    def get_absolute_url(self):
        return u'/materiaux/famille/{}'.format(self.reference)

    def __str__(self):
        return '{} - {}'.format(self.reference, self.matiere)
