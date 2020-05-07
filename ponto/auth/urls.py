from django.urls import path
from ponto.auth import views

app_name = 'auth'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user_details, name='user_details'),
    path('user-management/', views.user_management, name='user_management'),
    path('user-management/<int:id>/', views.user_management, name='user_management'),
]
