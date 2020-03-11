
from django.urls import path
from . import views



urlpatterns = [
    path('', views.vistaIndex, name='indexelecciones'),
    path('usuarios/', views.usuarios, name='usuarios'),
    
]
