from django.db import models


class Turno(models.Model):

    data = models.DateField(null=False)

    hora_chegada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)

    saida_almoço = models.TimeField()
    entrada_almoço = models.TimeField()

    presente = models.BooleanField()

    id_Funcionario = models.ForeignKey(Funcionario)