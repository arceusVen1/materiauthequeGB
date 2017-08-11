from django.db import models
import os
from django.conf import settings
from .sub_family import SubFamily
import qrcode


class Materiau(models.Model):

    class Meta:
        verbose_name = "Materiau"
        verbose_name_plural = "Materiaux"

    name = models.CharField(max_length=255)
    sub_family = models.ForeignKey(SubFamily)
    usage = models.TextField(default="N.R.")
    creation_date = models.DateField(null=True, blank=True, auto_now_add=True)
    available = models.BooleanField(blank=True, default=True)
    qr_code = models.ImageField(upload_to='materiaux', null=True, blank=True)

    @property
    def family(self):
        return self.sub_family.family

    @property
    def reference_number(self):
        return "MAT-{}-{}".format(self.sub_family, self.id)


    def generate_qrcode(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + self.id)
        qr = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(settings.SITE_URL + self.get_absolute_url())
        path = os.path.join(path, "qr_" + str(self.id) + ".jpg")
        qr.make_image().save(path)
        self.qr_code = "materiaux/{}/{}.jpg".format(str(self.id), str(self.id))

    def generate_folder(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + self.id)
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

    def compute_and_save(self):
        """
        used for creation and update. If the materiau sub family is changed it needs to change folder
        and the qr code to be regenerated

        """

        self.save()
        self.generate_folder()
        self.generate_qrcode()

    def get_absolute_url(self):
        return u'/materiaux/{}'.format(self.reference_number)

    def __str__(self):
        return self.reference_number