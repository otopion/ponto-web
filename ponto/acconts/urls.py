from django.urls import path
from ponto.acconts import views

app_name = 'acconts'
urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
