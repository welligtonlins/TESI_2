from django.contrib import messages
from django.shortcuts import render, redirect
from Juizes.models import Juiz
# Create your views here.
from Juizes.forms import JuizForms


def juizes(request):
    context ={
        'juizes': Juiz.objects.all()
    }
    return render(request, 'juizes.html', context)

def adiciona_juiz(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = JuizForms(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Juiz adicionado com sucesso!')
                forms = JuizForms()
            else:
                messages.error(request, 'Erro: Juiz não adicionado!')
        else:
            forms = JuizForms()

        context = {
            'form': forms
        }
        return render(request, 'adiciona_juiz.html', context)
    else:
        return redirect('juizes')