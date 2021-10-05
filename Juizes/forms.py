from django import forms

from Juizes.models import  Juiz

class JuizForms(forms.ModelForm):

    class Meta:
        model = Juiz
        fields = ['Juiz_Nome']