import email
from mailbox import NoSuchMailboxError
from django.db import models

class LeadTeam(models.Model):
      nombre = models.CharField( max_length=50)
      apellido = models.CharField( max_length=50)
      email = models.EmailField()
      paginaWeb = models.CharField( max_length=350)
      descripcion = models.TextField()
      Equipo  = models.IntegerField()
      
      
      
class Usuario(models.Model):
      nombre = models.CharField( max_length=50)
      apellido = models.CharField( max_length=50)
      email = models.EmailField()
      paginaWeb = models.CharField( max_length=350)
      descripcion = models.TextField()
      Equipo  = models.IntegerField()
      
