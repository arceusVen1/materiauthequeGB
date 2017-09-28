from django.contrib import admin
from django.utils.html import format_html

from .models import MateriauApprouve, Brouillon
from .models import SousFamille
from .models import Famille
from .models import Fournisseur
from .models import Propriete
from .models import Attribut
from .models import FormeMarchande
from .models import MiseEnForme
from .models import Traitement
from .models import Aspect
from .forms import MyMateriauAdminForm, MySousFamilleAdminForm, MyFamilyAdminForm


class AttributInline(admin.StackedInline):
    model = Attribut
    min_num = 1
    extra = True
    readonly_fields = ('materiau',)

@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):

    form = MyFamilyAdminForm
    list_display = ('reference', 'matiere',)
    readonly_fields = ('nombre_de_sous_famille',)


@admin.register(SousFamille)
class SousFamilleAdmin(admin.ModelAdmin):

    list_display = ('reference', 'matiere',)
    readonly_fields = ('reference', 'nombre_de_materiaux',)
    form = MySousFamilleAdminForm
    ordering = ['famille']


class MateriauAdmin(admin.ModelAdmin):
    """
    Abstract class for rerpresenting a materiaux (Appouve or Brouillon
    """
    list_display = ("reference", "nom", "fournisseur", "date_de_creation")
    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code', 'date_de_creation', 'reference', "site_web_du_fournisseur",)
    inlines = [
        AttributInline,
    ]
    form = MyMateriauAdminForm

    def site_web_du_fournisseur(self, obj):
        return format_html('<a href="{}">{}</a>',
                           obj.fournisseur.site_web,
                           obj.fournisseur.site_web,

                           )

    fieldsets = (
        ("Informations sur le materiau", {
            "fields": (
                "nom",
                "reference",
                "sous_famille",
                "brouillon",
                "date_de_creation",
                "disponible",
                "qr_code",
            )
        }),
        ("Fournisseur", {
            "fields": (
                "fournisseur",
                "site_web_du_fournisseur",
            )
        }),
        ("Usage", {
            "fields": (
                "forme_marchande",
                "usage",
                "mise_en_forme",
                "traitement",
            )
        }),
        ("Aspect", {
            "fields": (
            "aspect",
            )
        }),
        ("Ecologie", {
            "fields": (
                "empreinte_ecologique",
                "origine",
                "fin_de_vie",
            )
        }),
        ("Normes", {
            "fields": (
                "classement_au_feu",
                "classement_humidite",
                "classement_ecologique",
            )
        }),
        ("Commentaires", {
            "fields": (
                "commentaire",
            )
        })
    )


@admin.register(MateriauApprouve)
class MateriauxApprouveAdmin(MateriauAdmin):
    pass


@admin.register(Brouillon)
class BrouillonAdmin(MateriauAdmin):
    pass



@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):

    list_display = ('nom', 'site_web_url',)

    def site_web_url(self, obj):
        return format_html('<a href="{}">{}</a>',
                           obj.site_web,
                           obj.site_web,
                           )


@admin.register(Propriete)
class ProprieteAdmin(admin.ModelAdmin):

    list_display = ("nom", "unite", "type",)


@admin.register(FormeMarchande)
class FormeMarchandeAdmin(admin.ModelAdmin):
    pass


@admin.register(MiseEnForme)
class MiseEnFormeAdmin(admin.ModelAdmin):
    pass


@admin.register(Traitement)
class TraitementAdmin(admin.ModelAdmin):
    pass


@admin.register(Aspect)
class Aspect(admin.ModelAdmin):

    list_display = ("qualificatif", "type")
    ordering = ['type']



