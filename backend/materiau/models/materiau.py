from django.db import models
import os
from django.conf import settings
from .sous_famille import SousFamille
import qrcode


class Materiau(models.Model):

    class Meta:
        verbose_name = "Materiau"
        verbose_name_plural = "Materiaux"

    nom = models.CharField(max_length=255)
    sous_famille = models.ForeignKey(SousFamille)
    usage = models.TextField(default="N.R.")
    date_de_creation = models.DateField(null=True, blank=True, auto_now_add=True)
    disponible = models.BooleanField(blank=True, default=True)
    qr_code = models.ImageField(upload_to='materiaux', null=True, blank=True)

    @property
    def family(self):
        return self.sous_famille.famille

    @property
    def reference(self):
        return "MAT-{}-{}".format(self.sous_famille.reference, self.id)


    def generate_qrcode(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + str(self.id))
        qr = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(settings.SITE_URL + self.get_absolute_url())
        path = os.path.join(path, "qr_" + str(self.id) + ".jpg")
        qr.make_image().save(path)
        self.qr_code = "materiaux/{}/{}.jpg".format(str(self.id), str(self.id))

    def generate_folder(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + str(self.id))
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

    def compute_and_save(self):
        """
        used for creation and update. If the materiau sub famille is changed it needs to change folder
        and the qr code to be regenerated

        """

        self.save()
        self.generate_folder()
        self.generate_qrcode()

    def get_absolute_url(self):
        return u'/materiaux/{}'.format(self.reference)

    def __str__(self):
        return self.reference