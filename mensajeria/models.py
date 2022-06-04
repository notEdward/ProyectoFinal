from django.db import models

# Create your models here.
#---- Mensajeria ----
class Mensaje(models.Model):
    remitente_id = models.IntegerField()
    remitente_usuario = models.TextField(max_length=50) 
    destinatario_id = models.IntegerField()
    mensaje = models.TextField(max_length= 500)
    fecha = models.DateTimeField()
    visto = models.CharField(max_length=2)
