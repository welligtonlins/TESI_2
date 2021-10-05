from django.db import models
from stdimage import StdImageField
# Create your models here.
class Usuario(models.Model):
        User_Nome = models.CharField('Nome', max_length=60)
        User_Email = models.CharField('Email', max_length=60)
        User_Senha = models.CharField('Senha', max_length=20)
        User_Cel = models.CharField("Celular", max_length=15)
        User_Imagem = StdImageField('imagem', upload_to='usuarios', variations={'thumb':(90, 90)},  blank=True, null=True)

        def __str__(self):
                return self.User_Email