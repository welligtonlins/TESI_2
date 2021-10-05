from django.db import models

# Create your models here.
class Juiz(models.Model):

    Juiz_Nome = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.Juiz_Nome