from django.db import models


class Funcionario(models.Model):

    nome = models.CharField(max_length=50, null=False)
    sobre_nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=50, null=False)

    hora_chegada = models.TimeField(null=False)
    hora_saida = models.TimeField(null=False)
