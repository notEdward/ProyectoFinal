from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('', inicio),
path('formulario/', formulario, name="formulario"),
path('buscar/', buscar, name="buscar"),
path('resultados/', resultados, name="resultados"),
path('login', login_request, name="login" ),
path('register', register, name="register" ),
path('logout', LogoutView.as_view(template_name="AppDesafio/logout.html"), name='logout'),
path('agregar-post', agregarPost, name='agregar-post')

]

