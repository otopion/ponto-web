from django.urls import path
from ponto.acconts import views

app_name = 'auth'
urlpatterns = [
    path('cadastrar/', views.cadastar, name='cadastrar'),
]
