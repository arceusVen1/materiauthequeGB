from django.contrib import admin
from .models import MateriauApprouve, Brouillon
from .models import SousFamille
from .models import Famille
from .models import Fournisseur
from .models import Propriete
from .models import Attribut
from .models import FormeMarchande
from .models import MiseEnForme
from .forms import MyMateriauAdminForm, MySousFamilleAdminForm, MyFamilyAdminForm


class AttributInline(admin.StackedInline):
    model = Attribut
    min_num = 1
    extra = True
    readonly_fields = ('materiau',)

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
    inlines = [
        AttributInline,
    ]
    form = MyMateriauAdminForm


@admin.register(Brouillon)
class BrouillonAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code', 'date_de_creation',)
    inlines = [
        AttributInline,
    ]
    form = MyMateriauAdminForm


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):

    list_display = ('nom', 'site_web_url',)

    def site_web_url(self, obj):
        return '<a href="%s">%s</a>' % (obj.site_web, obj.site_web)

    site_web_url.allow_tags = True


@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):
    pass


@admin.register(FormeMarchande)
class FormeMarchandeAdmin(admin.ModelAdmin):
    pass

@admin.register(MiseEnForme)
class MiseEnForme(admin.ModelAdmin):
    pass



