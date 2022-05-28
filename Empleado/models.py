import email
from mailbox import NoSuchMailboxError
from django.db import models

class LiderDeEquipo(models.Model):
      nombre = models.CharField( max_length=50)
      apellido = models.CharField( max_length=50)
      email = models.EmailField()
      paginaWeb = models.CharField( max_length=350)
      descripcion = models.TextField()
      team  = models.IntegerField()
      
      
      
class Colaborador(models.Model):
      nombre = models.CharField( max_length=50)
      apellido = models.CharField( max_length=50)
      email = models.EmailField()
      paginaWeb = models.CharField( max_length=350)
      descripcion = models.TextField()
      team  = models.IntegerField()
      
class Equipo(models.Model):  
    nombre = models.CharField( max_length=50)
    team = models.IntegerField()


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)
    contenido = models.TextField()
    team = models.IntegerField()
    posteador = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.tema}] {self.titulo }"
