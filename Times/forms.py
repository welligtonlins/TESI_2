from django import forms

from Times.models import  Time

class TimeForms(forms.ModelForm):

    class Meta:
        model = Time
        exclude = ['Time_Pontos', 'Time_Vitorias',
        'Time_Empates', 'Time_Derrotas','Time_SaldoGols', 'Time_GolsFeitos', 'Time_GolsSofridos']