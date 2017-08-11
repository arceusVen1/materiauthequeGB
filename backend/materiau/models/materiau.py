from django.db import models
import os
from django.conf import settings
import qrcode


class Materiau(models.Model):

    class Meta:
        verbose_name = "Materiau"
        verbose_name_plural = "Materiaux"

    ref_number = models.CharField(max_length=6, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    sub_family = models.ForeignKey('SousFamille', verbose_name="Sous-famille")
    usage = models.TextField(default="N.R.")
    date = models.DateField(null=True, blank=True, auto_now_add=True)
    available = models.BooleanField(null=True, blank=True, default=True)
    qr_code = models.ImageField(upload_to='materiaux', null=True, blank=True)

    @property
    def family(self):
        return self.sub_family.family

    def folder_renaming(self, tampon):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux")
        if not os.path.exists(os.path.join(path, tampon)):
            return
        os.rename(os.path.join(path, tampon), os.path.join(path, self.ref_number))

    def generate_qrcode(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + self.ref_number)
        qr = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(settings.SITE_URL + self.get_absolute_url())
        path = os.path.join(path, self.ref_number + ".jpg")
        qr.make_image().save(path)
        self.qrcode = "materiaux/{}/{}.jpg".format(self.ref_number, self.ref_number)

    def generate_folder(self):
        path = os.path.join(settings.MEDIA_ROOT, "materiaux/" + self.slug)
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

    def compute_and_save(self):
        """
        used for creation and update. If the materiau sub family is changed it needs to change folder
        and the qr code to be regenerated

        """

        # if its an update the ref_number is saved to be reused

        tampon = self.ref_number

        self.ref_number = "MAT" + "-" + self.sub_family + "-"

        # the ref_number uses the last db id + 1

        if self.id is None:
            try:
                last = Materiau.objects.last()
                self.id = last.id + 1
            except AttributeError:
                self.id = 0

        # append the id to the ref_number

        self.ref_number += str(self.id)

        # the folder renaming and qr code regen if necessary

        if self.ref_number != tampon:
            if tampon is not None:
                try:
                    os.remove(os.path.join(settings.MEDIA_ROOT, str(self.qrcode)))
                except OSError as e:
                    print(e)
                self.folder_renaming(tampon)
            self.generate_folder()
            self.generate_qrcode()
        self.save()

    def get_absolute_url(self):
        return u'/materiaux/{}'.format(self.slug)

    def __str__(self):
        return self.ref_number