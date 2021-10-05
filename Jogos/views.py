from django.contrib import messages
from django.shortcuts import render, redirect
from Jogos.forms import JogoForms
from Jogos.models import Jogo
from Juizes.models import Juiz
# Create your views here.

def adiciona_jogo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = JogoForms(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Jogo adicionado com sucesso!')
                forms = JogoForms()
            else:
             messages.error(request, 'Erro ao adicionar jogo!')
        else:
            forms = JogoForms()
        context = {
            'form' : forms
        }
        return render(request, 'adiciona_jogo.html', context)
    else:
        return redirect('jogos')

def jogos(request):
    context ={
        'jogos': Jogo.objects.all()
    }
    
    return render(request, 'jogos.html', context)
