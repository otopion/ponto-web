from django.contrib import admin

from .models.Funcionario.funcionario import Funcionario
from .models.Funcionario.turno import Turno

admin.site.register(Funcionario)
admin.site.register(Turno)