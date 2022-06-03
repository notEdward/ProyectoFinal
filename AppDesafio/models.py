from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

class Animal(models.Model):
    especie = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    fecha_ingreso = models.DateField()

class Persona(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Donacion(models.Model):
    monto = models.IntegerField()
    nota_donacion = models.CharField(max_length=30, default = '')


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('posteos/', filename)

class Item(models.Model):
    usuarioCreador = models.TextField(max_length=50)
    fecha =  models.DateField()
    titulo = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to=filepath, null=True, blank=True)

#---- Comentarios ----
class Comentario(models.Model):
    usuario = models.TextField(max_length=50)
    comentario = models.TextField(max_length= 500)
    fecha = models.DateField()
    posteoId = models.IntegerField()

#----Perfil-------
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatar', blank=True, null=True)
