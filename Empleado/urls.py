from django.urls import path
from os import name

from django.urls import clear_script_prefix
from . import views
from django.urls import path, include 
urlpatterns = [
  
  path ('Nuevo_LiderEquipo', views.LiderNuevo, name='Nuevo Lider'),
  path ('Nuevo_Colaborador', views.Colaborador, name='Nuevo Colaborador'),
  path ('Nuevo_Equipo', views.Equipo, name='Nuevo Team'),
  path("", views.Inicio, name="InicioPags"),
  path("Buscar/<post>", views.buscar_equipo, name="Buscar Post"),
   
]
