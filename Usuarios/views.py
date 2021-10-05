from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from Usuarios.forms import UsuarioForms
from Usuarios.models import Usuario

def pagina_usuario(request):
    context ={
        'usuario': Usuario
    }
    return render(request, 'pagina_usuario.html',context)

def cadastra_usuario(request):
    if request.method == 'POST':
        forms = UsuarioForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Usuário cadastrado com sucesso !')
            forms = UsuarioForms()
        else:
            messages.error(request, 'Erro ao cadastrar usuário !')
    else:
        forms = UsuarioForms()
    context = {
        'form' : forms

    }
    return  render(request,'cadastra_usuario.html', context)

def login(request):
    return render(request, 'login.html')