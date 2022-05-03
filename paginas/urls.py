from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioPags"),
    path("buscar/<team>", views.buscar_team, name="Buscar Hilo"),
]