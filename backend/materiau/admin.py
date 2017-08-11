from django.contrib import admin
from .models.materiau import Materiau
from .models.sous_famille import SousFamille
from .models.famille import Famille


@admin.register(Famille)
class MateriauAdmin(admin.ModelAdmin):
    pass


@admin.register(SousFamille)
class MateriauAdmin(admin.ModelAdmin):
    pass


@admin.register(Materiau)
class MateriauAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code',)