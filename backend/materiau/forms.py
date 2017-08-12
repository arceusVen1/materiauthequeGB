from django import forms
from .models.materiau import Materiau
from .models.sous_famille import SousFamille
from .models.famille import Famille


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