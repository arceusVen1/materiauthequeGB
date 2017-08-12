from django.contrib import admin
from .models.materiau import Materiau, MateriauApprouve, Brouillon
from .models.sous_famille import SousFamille
from .models.famille import Famille
from .models.fournisseur import Fournisseur
from django import forms


class MyFamilyAdminForm(forms.ModelForm):

    class Meta:
        model = Famille
        fields = '__all__'

    def clean_reference(self):
        return self.cleaned_data['reference'].upper()

    def clean_matiere(self):
        return self.cleaned_data['matiere'].upper()


class MySousFamilleAdminForm(forms.ModelForm):

    class Meta:
        model = SousFamille
        exclude = ['numero_de_reference',]

    def clean_matiere(self):
        return self.cleaned_data['matiere'].upper()


class MyMateriauAdminForm(forms.ModelForm):

    class Meta:
        model = Materiau
        exclude = ('qr_code', 'date_de_creation',)

    def clean_nom(self):
        return self.cleaned_data['nom'].title()


@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):

    form = MyFamilyAdminForm


@admin.register(SousFamille)
class SousFamilleAdmin(admin.ModelAdmin):

    readonly_fields = ('reference',)
    form = MySousFamilleAdminForm


@admin.register(MateriauApprouve)
class MateriauApproveAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code', 'date_de_creation',)
    form = MyMateriauAdminForm


@admin.register(Brouillon)
class BrouillonAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code', 'date_de_creation',)
    form = MyMateriauAdminForm


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):

    list_display = ('nom', 'site_web_url',)

    def site_web_url(self, obj):
        return '<a href="%s">%s</a>' % (obj.site_web, obj.site_web)

    site_web_url.allow_tags = True
