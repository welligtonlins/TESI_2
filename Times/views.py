from django.contrib import messages
from django.shortcuts import render, redirect
from Times.forms import TimeForms

from Times.models import Time
# Create your views here.
#def index(request):
  #  return render(request, 'index.html')

def dados_time(request):
    context = {
        'times':Time.objects.all()
    }
    return render(request, 'dados_time.html',context)

def adiciona_time(request):
    if request.user.is_authenticated:
        time = Time(Time_Pontos=0, Time_Vitorias=0, Time_Empates=0, Time_Derrotas=0,
                Time_SaldoGols=0, Time_GolsFeitos=0, Time_GolsSofridos=0)
        if request.method == 'POST':
            forms = TimeForms(request.POST, request.FILES, instance=time)
            if forms.is_valid():
                forms.save()
                messages.success(request, 'Time adicionado com sucesso !')
                forms = TimeForms()
            else:
                messages.error(request, 'Erro: Time não adicionado !')

        else:
            forms = TimeForms()

        context = {
            'form': forms
        }
        return render(request, 'adiciona_time.html', context)
    else:
        return redirect('dados_time')