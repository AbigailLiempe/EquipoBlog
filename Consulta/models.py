from unittest.util import _MAX_LENGTH
from django.db import models


class Consulta(models.Model):
    Titulo = models.CharField(max_length=255)
    Tema = models.CharField(max_length=255)
    Contenido = models.TextField()
    Equipo = models.IntegerField()
    Posteador = models.CharField(max_length=255)
