from django.urls import path
from .views import *

urlpatterns = [

path('', inicio),
path('formulario/', formulario, name="formulario"),
path('buscar/', buscar, name="buscar"),
path('resultados/', resultados, name="resultados"),
path('login', login_request, name="login" ),
path('register', register, name="register" ),
]
