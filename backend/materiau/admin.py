from django.contrib import admin
from .models.materiau import Materiau


@admin.register(Materiau)
class MateriauAdmin(admin.ModelAdmin):

    date_hierarchy = 'creation_date'
    readonly_fields = ('qr_code',)
