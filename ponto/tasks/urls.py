from django.urls import path
from ponto.tasks import views

urlpatterns = [
    path('turno/', views.turno, name='turno'),
    path('turno/<int:pk>/', views.turno, name='turno'),
    path('funcionario/', views.funcionario, name='funcionario'),
    path('funcionario/<int:pk>/', views.funcionario, name='funcionario'),
]