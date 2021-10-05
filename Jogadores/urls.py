from django.urls import path

from Jogadores.views import jogadores, adiciona_jogador

urlpartterns = [
    path('jogadores', jogadores, name='jogadores'),
    path('adiciona_jogador', adiciona_jogador, name='adiciona_jogador'),
]
