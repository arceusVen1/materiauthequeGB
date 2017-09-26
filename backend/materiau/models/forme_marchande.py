from django.db import models


class FormeMarchande(models.Model):

    type = models.CharField(max_length=255, unique=True)
