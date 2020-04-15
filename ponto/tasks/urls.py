from django.urls import path, include

from rest_framework import routers
from ponto.tasks.views import TurnoViewSet, FuncionarioViewSet

router = routers.DefaultRouter()
router.register('turno', TurnoViewSet)
router.register('funcionario', FuncionarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
]