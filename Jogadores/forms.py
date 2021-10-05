from django import forms

from Jogadores.models import Jogador
class JogadorForms(forms.ModelForm):
    class Meta:
        model = Jogador
        exclude = ['Jogador_Gols', 'Jogador_CartaoAmarelo', 'Jogador_CartaoVermelho']
        #fields = ['Jogador_Nome', 'Jogador_Cpf', 'Jogador_Time']