
from django.urls import path
from . import views



urlpatterns = [
    path('', views.vistaIndex, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),

]
