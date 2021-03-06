from django.urls import path
from ponto.tasks import views

app_name = 'tasks'
urlpatterns = [
    path('turno-management/', views.turno_ma, name='turno-management'),
    path('turno-management/<int:pk>/', views.turno_ma, name='turno-management'),
    path('turno/', views.turno, name='turno'),
    path('funcionario-management/', views.funcionario_ma, name='funcionario-management'),
    path('funcionario-management/<int:pk>/', views.funcionario_ma, name='funcionario-management'),
    path('funcionario/', views.funcionario, name='funcionario'),
]