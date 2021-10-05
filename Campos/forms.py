from django import forms
from Campos.models import Campo
class CampoForms(forms.ModelForm):
    class Meta:
        model = Campo
        fields = ['Campo_Nome', 'Campo_End', 'Campo_Maps']
