from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('', inicio),
# path('formulario/', formulario, name="formulario"),
# path('buscar/', buscar, name="buscar"),
# path('resultados/', resultados, name="resultados"),

#----LOGIN-----
path('login', login_request, name="login" ),
path('register', register, name="register" ),
path('logout', LogoutView.as_view(template_name="AppDesafio/logout.html"), name='logout'),

#----PERFIL-----
path('editarPerfil', editarPerfil, name='editarPerfil'),
path('agregarAvatar', agregarAvatar, name='agregarAvatar'),

#-----POSTEOS-----
path('agregar-post', agregarPost, name='agregar-post'),
path('editar-post/<str:pk>', editarPost, name='editar-post'),
path('comentar-post/<str:pk>', comentarPost, name='comentar-post'),
path('mis-post', verPost, name='mis-post'),


]

