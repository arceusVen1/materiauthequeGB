from django.contrib import admin
from django.utils.html import format_html

from .forms import MyPackagingAdminForm
from .models import PackagingApprouve, Brouillon, Marque, Impression, Finition


# Register your models here.
class PackagingAdmin(admin.ModelAdmin):

    def site_web_de_la_marque(self, obj):
        return format_html('<a href="{}">{}</a>',
                           obj.marque.site_web,
                           obj.marque.site_web,
                           )

    form = MyPackagingAdminForm

    readonly_fields = ("reference",
                       "qr_code",
                       "site_web_de_la_marque",
                       "date_de_creation",
                       )
    fieldsets = (
        ("Informations sur le packaging", {
            "fields": (
                "nom",
                "reference",
                "date_de_creation",
                "brouillon",
                "description",
                "qr_code",
            ),
        }),
        ("Marque", {
            "fields": (
                "marque",
                "site_web_de_la_marque",
            ),
        }),
        ("Caractéristiques", {
            "fields": (
                "materiaux",
                "fabrication",
                "mise_en_forme",
                "impression",
                "finition",
            )
        }),
        ("Commentaires", {
            "fields": (
                "commentaire",
            )
        }),
    )


@admin.register(PackagingApprouve)
class PackagingApprouveAdmin(PackagingAdmin):
    pass


@admin.register(Brouillon)
class BrouillonAdmin(PackagingAdmin):
    pass


@admin.register(Marque)
class MarqueAdmin(admin.ModelAdmin):
    pass


@admin.register(Impression)
class ImpressionAdmin(admin.ModelAdmin):
    pass


@admin.register(Finition)
class FinitionAdmin(admin.ModelAdmin):
    pass
