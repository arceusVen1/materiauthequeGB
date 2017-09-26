from django.db import models


class MiseEnForme(models.Model):

    type = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.type = self.type.title()
        super().save()

    def __str__(self):
        return self.type