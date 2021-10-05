

from django.db import models
from Times.models import Time
from Juizes.models import Juiz
from Campos.models import Campo
from datetime import datetime

class Jogo(models.Model):

    Jogo_Time = models.ManyToManyField(Time)
    Jogo_Data= models.DateTimeField('Data/Hora')
    Jogo_Campo = models.ForeignKey(Campo, on_delete=models.CASCADE)
    Jogo_Juiz = models.ForeignKey(Juiz, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)

