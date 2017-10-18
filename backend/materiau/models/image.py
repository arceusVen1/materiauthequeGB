from django.db import models
import os
from django.conf import settings
from .materiau import Materiau


class Image(models.Model):

    def image_file_name(self, filename):
        return "materiau/{}/{}".format(self.materiau.nom, filename)

    legende = models.CharField(null=True, blank=True, max_length=255, verbose_name="Légende")
    imagefile = models.ImageField(upload_to=image_file_name, null=True, blank=True, verbose_name='Image')
    materiau = models.ForeignKey(Materiau, null=True, blank=True, verbose_name="Matériau associé")

    def save(self):
        super(Image, self).save()

    def delete(self):
        os.remove(os.path.join(settings.MEDIA_ROOT, str(self.imagefile)))
        super().delete()
