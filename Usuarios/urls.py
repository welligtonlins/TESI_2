from django.urls import path

from Usuarios.views import pagina_usuario, cadastra_usuario, login

urlpatterns = [
    path('pagina_usuario', pagina_usuario, name='pagina_usuario'),
    path('cadastra_usuario', cadastra_usuario, name='cadastra_usuario'),
    path('login', login, name='login'),
]