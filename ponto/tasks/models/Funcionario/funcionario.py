from django.db import models
from django.contrib.auth.models import User


class Funcionario(models.Model):
    user = models.OneToOneField(User, related_name='funcionario', on_delete=models.CASCADE)
    hora_chegada = models.TimeField()
    hora_saida = models.TimeField()

