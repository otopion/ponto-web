from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models.Funcionario.turno import Turno
from .models.Funcionario.funcionario import Funcionario
from .serializers.Funcionario.turno import TurnoSerializer
from .serializers.Funcionario.funcionario import FuncionarioSerializer


class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

