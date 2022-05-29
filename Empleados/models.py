from django.db import models
import email
from mailbox import NoSuchMailboxError
from django.db import models
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Lider(models.Model):
      
    def __str__(self):
      return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Area: {self.area}"
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    area = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = "Lider"
        verbose_name_plural = "Lideres"
      
      
class Colaborador(models.Model):
      nombre = models.CharField( max_length=50)
      apellido = models.CharField( max_length=50)
      email = models.EmailField()
      paginaWeb = models.CharField( max_length=350)
      descripcion = models.TextField()
      equipo  = models.IntegerField()
      
class Equipo(models.Model):  
    nombre = models.CharField( max_length=50)
    equipo = models.IntegerField()
    duracion = models.IntegerField(default=0)


class Post(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)
    contenido = models.TextField()
    equipo = models.IntegerField()
    posteador = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.tema}] {self.titulo }"


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null=True, blank=True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"