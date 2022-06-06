from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
#---- Mensajeria ----
class Mensaje(models.Model):
    remitente_id = models.IntegerField()
    remitente_usuario = models.TextField(max_length=50) 
    destinatario_id = models.IntegerField()
    destinatario_usuario = models.TextField(max_length=50) 
    mensaje = models.TextField(max_length= 500)
    fecha = models.DateTimeField()
    visto = models.CharField(max_length=2)

class Anuncio(models.Model):
    creador_id= models.IntegerField()
    creador_usuario = models.TextField(max_length=50)
    mensaje = tinymce_models.HTMLField()
    fecha = models.DateTimeField()

    def __str__(self):
        return "Anuncio de " + self.creador_usuario