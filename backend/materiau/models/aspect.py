from django.db import models


class Aspect(models.Model):

    type = models.CharField(max_length=255)
    qualificatif = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.type = self.type.title()
        self.qualificatif = self.qualificatif.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.type, self.qualificatif)