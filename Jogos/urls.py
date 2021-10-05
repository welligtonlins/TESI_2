from django.urls import path
from Jogos.views import adiciona_jogo, jogos
urlspatterns = [
    path('adiciona_jogo', adiciona_jogo, name='adiciona_jogo'),
    path('jogos', jogos, name='jogos'),
]