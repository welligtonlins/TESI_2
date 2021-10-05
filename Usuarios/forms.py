from django import forms

from Usuarios.models import Usuario


class UsuarioForms(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['User_Nome', 'User_Email', 'User_Senha', 'User_Cel', 'User_Imagem' ]
