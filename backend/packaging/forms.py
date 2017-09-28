from django import forms
from .models import Packaging


class MyPackagingAdminForm(forms.ModelForm):

    class Meta:
        model = Packaging
        exclude = ('reference', 'qr_code', 'date_de_creation',)

    def clean_nom(self):
        return self.cleaned_data['nom'].title()