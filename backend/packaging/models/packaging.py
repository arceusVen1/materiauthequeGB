from django.db import models
from materiau.models import Materiau, BrouillonManager, ApprouveManager
import os
import qrcode
from materiautheque import settings
from .marque import Marque


class Packaging(models.Model):

    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    brouillon = models.BooleanField(blank=True)
    nom_produit = models.CharField(verbose_name="Nom du produit", max_length=255, blank=True)
    materiaux = models.ManyToManyField(Materiau, blank=True)
    fabrication = models.TextField(verbose_name="Procédé de fabrication", blank=True, null=True)
    mise_en_forme = models.TextField(blank=True, null=True)
    qr_code = models.ImageField(upload_to='packagings', null=True, blank=True)
    commentaire = models.TextField(blank=True, null=True)
    marque = models.ForeignKey(Marque, blank=True, null=True)

    def generate_qr_code(self):
        path = os.path.join(settings.MEDIA_ROOT, "packagings/" + str(self.id))
        qr = qrcode.QRCode(version=20, error_correction=qrcode.constants.ERROR_CORRECT_L)
        qr.add_data(settings.SITE_URL + self.get_absolute_url())
        path = os.path.join(path, "qr_" + str(self.id) + ".jpg")
        qr.make_image().save(path)
        self.qr_code = "packagings/{}/qr_{}.jpg".format(str(self.id), str(self.id))

    def generate_folder(self):
        """
        generate a folder for the media of a packaging in media/packagings/
        named by the id of the packaging. The id never changes so no need to recall this function after first save
        """
        path = os.path.join(settings.MEDIA_ROOT, "packagings/" + str(self.id))
        try:
            os.makedirs(path)
        except OSError as e:
            print(e)

    def get_absolute_url(self):
        return u'/packagings/{}'.format(self.reference)

    def save(self, *args, **kwargs):
        """
        used for creation and update.

        """
        self.nom = self.nom.title()

        # if its a brouillon there is no more computation so save and return

        if self.brouillon:
            super().save()
            return

        # we need to get the id of the packaging first before generating its folder and qr code so we save it once

        if self.id is None:
            super().save()

        # then we generate the qr code  and folder
        # we call generate folder for each save in case a brouillon is turned into a "packaging approuvé"

        self.generate_folder()
        self.generate_qr_code()
        super().save()


class Brouillon(Packaging):

    class Meta:
        proxy = True
        verbose_name_plural = "Brouillons"

    objects = BrouillonManager()


class PackagingApprouve(Packaging):

    class Meta:
        proxy = True
        verbose_name_plural = "Packagings approuvés"

    objects = ApprouveManager()
