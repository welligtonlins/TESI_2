from django.db import models

# Create your models here.
class Campo(models.Model):

    Campo_Nome = models.CharField('Nome', max_length=60)
    Campo_End = models.CharField('Endereco', max_length=100)
    Campo_Maps = models.CharField('Link_Maps', max_length=200)

    def __str__(self):
        return self.Campo_Nome