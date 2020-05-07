from django.urls import path
from ponto.tasks import views

urlpatterns = [
    path('turno-management/', views.turno, name='turno-management'),
    path('turno-management/<int:pk>/', views.turno, name='turno-management'),
    path('funcionario-management/', views.funcionario_ma, name='funcionario-management'),
    path('funcionario-management/<int:pk>/', views.funcionario_ma, name='funcionario-management'),
    path('funcionario/', views.funcionario, name='funcionario'),
]