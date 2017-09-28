from django.contrib import admin
from django.utils.html import format_html

from .models import Packaging, Marque

# Register your models here.

@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):

    def site_web_de_la_marque(self, obj):
        return format_html('<a href="{}">{}</a>',
                           obj.marque.site_web,
                           obj.marque.site_web,
                           )

    readonly_fields = ("site_web_de_la_marque",)
    fieldsets = (
        ("Informations sur le packaging", {
            "fields": (
                "nom",
                "reference",
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
            )
        }),
        (None, {
            "fields": (
                "commentaire",
            )
        }),
    )


@admin.register(Marque)
class MarqueAdmin(admin.ModelAdmin):
    pass