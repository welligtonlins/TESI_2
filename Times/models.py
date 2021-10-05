from django.db import models
from stdimage import StdImageField
# Create your models here.
class Time(models.Model):

    Time_Nome = models.CharField('Nome', max_length=50)
    Time_Pontos = models.IntegerField('Pontos')
    Time_Vitorias = models.IntegerField('Vitorias')
    Time_Empates = models.IntegerField('Empates')
    Time_Derrotas = models.IntegerField('Derrotas')
    Time_SaldoGols = models.IntegerField('SG')
    Time_GolsFeitos = models.IntegerField('GF')
    Time_GolsSofridos = models.IntegerField('GS')
    Time_Treinador = models.CharField('Treinador', max_length=30)

    Time_Imagem = StdImageField('imagem', upload_to='times', variations={'thumb':(90, 90)},  blank=True, null=True)
    def __str__(self):
        return "{}".format(self.Time_Nome)