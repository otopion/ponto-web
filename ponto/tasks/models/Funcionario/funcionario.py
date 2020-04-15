from django.db import models


class Funcionario(models.Model):

    nome = models.CharField(max_length=50)
    sobre_nome = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=50)

    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()
