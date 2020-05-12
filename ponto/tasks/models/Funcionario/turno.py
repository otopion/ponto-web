from django.db import models

from .funcionario import Funcionario


class Turno(models.Model):

    data = models.DateField(null=False)

    hora_chegada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)

    saida_almoco = models.TimeField()
    entrada_almoco = models.TimeField()

    presente = models.BooleanField()

    id_Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
