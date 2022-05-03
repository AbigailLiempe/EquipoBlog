from django.db import models


class Hilo(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)
    contenido = models.TextField()
    team = models.IntegerField()
    posteador = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.tema}] {self.titulo }"
