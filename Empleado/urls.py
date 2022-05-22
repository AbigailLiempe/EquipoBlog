from django.urls import path
from os import name

from django.urls import clear_script_prefix
from . import views
urlpatterns = [
  path ('',views.inicio,name='Inicio Empleado'),
  path ('Nuevo_LiderEquipo', views.Lidernuevo, name='Nuevo Lider'),
  path ('Nuevo_Colaborador', views.Colaborador, name='Nuevo Colaborador'),
  path ('Nuevo_Equipo', views.Teams, name='Nuevo Team')
]