from django.db import models


class Finition(models.Model):

    type = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.type = self.type.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.type
