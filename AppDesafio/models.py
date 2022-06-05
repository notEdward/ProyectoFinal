from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%d%m%Y%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('posteos/', filename)

class Posteo(models.Model):
    usuarioCreador = models.TextField(max_length=50)
    fecha =  models.DateField()
    titulo = models.TextField(max_length=50)
    subtitulo = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to=filepath, null=True, blank=True)

    def __str__(self):
        return "Posteo de " + self.usuarioCreador + " publicado el " + str(self.fecha)

#---- Comentarios ----
class Comentario(models.Model):
    usuario = models.TextField(max_length=50)
    user_id = models.IntegerField()
    comentario = models.TextField(max_length= 500)
    fecha = models.DateTimeField()
    posteoId = models.IntegerField()

#----Perfil-------
class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatar', blank=True, null=True)
