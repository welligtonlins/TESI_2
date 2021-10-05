
from django.db import models
from Times.models import Time
# Create your models here.
class Jogador(models.Model):

    Jogador_Nome = models.CharField('Nome', max_length=40)
    Jogador_Cpf = models.CharField('Cpf', max_length=14 )
    Jogador_Gols = models.IntegerField('Gols')
    Jogador_CartaoAmarelo = models.IntegerField('Cartão Amarelo')
    Jogador_CartaoVermelho = models.IntegerField('Cartão Vermelho')
    Jogador_Time = models.ForeignKey( Time, on_delete=models.CASCADE)

    def __str__(self):
        return self.Jogador_Nome