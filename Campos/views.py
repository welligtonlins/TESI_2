from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Campos.forms import CampoForms
from Campos.models import Campo
# Create your views here.
def campos(request):
    context = {
        'campos': Campo.objects.all()
    }
    return render(request, 'campos.html',context)

def c1(request):
   return render(request, 'c1.html')

def adiciona_campo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = CampoForms(request.POST)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Campo adicionado com sucesso!')
                forms = CampoForms()
            else:
                messages.error(request, 'Erro ao adicionar campo!')

        else:
            forms = CampoForms()

        context = {
            'form' : forms
        }
        return render(request, 'adiciona_campo.html', context)
    else:
        return redirect('lista_campos')