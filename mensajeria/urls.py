from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('mensajeria', mensajeria, name="mensajeria"),
path('mensajeria/enviarMensaje', enviarMensaje, name="enviarMensaje"),
path('mensajeria/verEnviados', verEnviados, name="verEnviados"),
path('anuncios', AnunciosList.as_view(), name="anuncios_listar"),

]

