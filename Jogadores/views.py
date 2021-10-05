from django.contrib import messages
from django.shortcuts import render, redirect

from Jogadores.models import Jogador
from Jogadores.forms import JogadorForms
# Create your views here.
def jogadores(request):
    context= {
        'jogadores': Jogador.objects.all()
    }
    return render(request, 'jogadores.html', context)

def adiciona_jogador(request):
    if request.user.is_authenticated:
        jogador = Jogador(Jogador_Gols=0, Jogador_CartaoAmarelo=0, Jogador_CartaoVermelho =0)
        if request.method == 'POST':
            forms = JogadorForms(request.POST, instance=jogador)
            if forms.is_valid():
                forms.save()
                messages.success(request,'Jogador adicionado com sucesso!')
                forms = JogadorForms()
            else:
                messages.error(request, 'Erro ao adicionar jogador')
        else:
            forms = JogadorForms()

        context = {
        'form': forms
        }
        return render(request, 'adiciona_jogador.html', context)
    else:
        return redirect('jogadores')