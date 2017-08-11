from django.contrib import admin
from .models.materiau import Materiau
from .models.sous_famille import SousFamille
from .models.famille import Famille
from django import forms

class MyFamilyAdminForm(forms.ModelForm):

    class Meta:
        model = Famille
        fields = '__all__'

    def clean_reference(self):
        return self.cleaned_data['reference'].upper()

    def clean_matiere(self):
        return self.cleaned_data['matiere'].upper()


@admin.register(Famille)
class FamilleAdmin(admin.ModelAdmin):

    form = MyFamilyAdminForm


@admin.register(SousFamille)
class SousFamilleAdmin(admin.ModelAdmin):
    readonly_fields = ('reference',)



@admin.register(Materiau)
class MateriauAdmin(admin.ModelAdmin):

    date_hierarchy = 'date_de_creation'
    readonly_fields = ('qr_code', 'date_de_creation',)
