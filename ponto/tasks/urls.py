from django.urls import path, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('turno', TurnoViewSet)
router.register('funcionario', FuncionarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
]