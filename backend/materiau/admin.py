from django.contrib import admin
from .models.materiau import MateriauApprouve, Brouillon
from .models.sous_famille import SousFamille
from .models.famille import Famille
from .models.fournisseur import Fournisseur
from .forms import MyMateriauAdminForm, MySousFamilleAdminForm, MyFamilyAdminForm


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
