from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib import admin 
urlpatterns = [

#Mensajeria
path('mensajeria', mensajeria, name="mensajeria"),
path('mensajeria/enviarMensaje/<str:pk>', enviarMensaje, name="enviarMensaje"),
path('mensajeria/enviarMensaje/', enviarMensaje, name="enviarMensaje"),
path('mensajeria/verEnviados', verEnviados, name="verEnviados"),
path('mensajeria/verNoLeidos', verNoLeidos, name="verNoLeidos"),
path('mensajeria/marcarLeido/<str:pk>', marcarLeido, name="marcarLeido"),

# path('anuncios', AnunciosList.as_view(), name="anuncios"),
#Anuncios
path('anuncios', verAnuncios, name="anuncios"),
path('anuncios/nuevoAnuncio', nuevoAnuncio, name="nuevoAnuncio"),

path('tinymce/', include('tinymce.urls')),
#-----USUARIOS----
path('usuarios', UsuariosList.as_view(), name="usuarios"),
]

