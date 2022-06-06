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
path('editarPerfil/agregarAvatar', agregarAvatar, name='agregarAvatar'),

#-----POSTEOS-----
path('agregarPost', agregarPost, name='agregarPost'),
path('editarPost/<str:pk>', editarPost, name='editarPost'),
path('borrarPost/<str:pk>', borrarPost, name='borrarPost'),
path('comentarPost/<str:pk>', comentarPost, name='comentarPost'),
path('verPost', verPost, name='verPost'),

#-----ABOUT------
path('about', about, name='about'),
#----PAGES------
path('pages', pages, name='pages'),
path('pages/<str:pk>', detallePost, name="detallePost"),

]

