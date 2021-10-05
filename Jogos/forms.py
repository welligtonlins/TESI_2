from django import forms
from Jogos.models import Jogo

class JogoForms(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['Jogo_Time', 'Jogo_Data', 'Jogo_Campo', 'Jogo_Juiz']