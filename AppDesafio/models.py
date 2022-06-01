from django.db import models

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