import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from AppDesafio.forms import UserRegistrationForm, UserEditForm, AvatarForm
from mensajeria.models import Anuncio, Mensaje
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.views.generic import ListView

import os


#Inicio
def inicio(request):

    posteos = Posteo.objects.all().order_by('id').reverse()
    anuncio = Anuncio.objects.last()
    #verifico mensajes sin leer para avisarle al usuario que tiene mensajes no leidos. 
    if request.user.is_authenticated:      
        unread = Mensaje.objects.filter(destinatario_id=request.user.id, visto='N').count()   
        avatar = Avatar.objects.filter(user=request.user)
        if avatar:
            if unread > 0 :
                return render(request, 'AppDesafio/inicio.html', {'posteos': posteos, 'anuncio':anuncio, 'unread':unread, 'url':avatar[0].avatar.url })

            return render(request, 'AppDesafio/inicio.html', {'posteos': posteos, 'anuncio':anuncio, 'url':avatar[0].avatar.url })     
    
    return render(request, 'AppDesafio/inicio.html', {'posteos': posteos, 'anuncio': anuncio})    

#---- Posteos ----
#---- AGREGAR -----
@login_required
def agregarPost(request):
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
    if request.method == "POST":
        posteo = Posteo()
        posteo.usuarioCreador = request.user
        posteo.fecha = datetime.datetime.now()
        posteo.titulo = request.POST.get('titulo')
        posteo.subtitulo = request.POST.get('genero')
        posteo.descripcion = request.POST.get('descripcion')

        if len(request.FILES) != 0:
            posteo.imagen = request.FILES['imagen']
        try:
         posteo.save()
        except:
         return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Error en los datos.','error':'error', 'url':avatar[0].avatar.url })
         
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Posteo creado exitosamente.', 'success':'success','url':avatar[0].avatar.url })

    return render(request, 'AppDesafio/nuevoPost.html', {'url':avatar[0].avatar.url})        
#---- EDICION -----
@login_required
def editarPost(request, pk):

    avatar = Avatar.objects.filter(user=request.user)
    try:
        posteo = Posteo.objects.get(id=pk)
    except:
        return render(request, 'AppDesafio/inicio.html', {'mensaje': 'No hay páginas aún', 'error':'error', 'url':avatar[0].avatar.url} ) 

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(posteo.imagen) > 0:
                os.remove(posteo.imagen.path)
            posteo.imagen = request.FILES['imagen']
        posteo.titulo = request.POST.get('titulo')
        posteo.subtitulo = request.POST.get('genero')
        posteo.descripcion = request.POST.get('descripcion')
        try:
         posteo.save()
        except:
         return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Error en los datos.','error':'error', 'url':avatar[0].avatar.url })

        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Posteo editado exitosamente.','success':'success', 'url':avatar[0].avatar.url })

    return render(request, 'AppDesafio/editPost.html', {'posteo': posteo, 'url':avatar[0].avatar.url})

#-----BORRADO-------    
@login_required
def borrarPost(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    posteo = Posteo.objects.get(id=pk)
    user = request.user
#si no es el posteo creado por el mismo usuario
    if posteo.usuarioCreador != user.username:
#chequeo si el usuario se encuentra en el grupo de usuarios comunes.
        if user.groups.filter(name='Usuarios_Comunes').exists():
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO PERMITIDO.', 'error':'error','url':avatar[0].avatar.url })
    if len(posteo.imagen) > 0 :
        os.remove(posteo.imagen.path)
    posteo.delete()
    return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Posteo eliminado exitosamente.', 'success':'success','url':avatar[0].avatar.url })

#----- VER -----
@login_required
def verPost(request):
    
    user=User.objects.get(username=request.user)
    avatar = Avatar.objects.filter(user=request.user)
    #obtenemos posteos del ultimo al primero
    posteos = Posteo.objects.filter(usuarioCreador=user).order_by('id').reverse()
    if avatar:
         return render(request, 'AppDesafio/misPost.html', {'posteos': posteos, 'url':avatar[0].avatar.url})    

    return render(request, 'AppDesafio/misPost.html', {'posteos': posteos})    

#----- COMENTAR ----
@login_required
def comentarPost(request, pk):

    avatar = Avatar.objects.filter(user=request.user)
    posteo = Posteo.objects.get(id=pk)
    comentarios = Comentario.objects.filter(posteoId = pk)
    avatarComentario = Avatar.objects.all()
    usuario = request.user
    usuario_id = request.user.id

    if request.method=="POST":
        comentario = Comentario(usuario = usuario, user_id = usuario_id, comentario = request.POST['texto'], fecha = datetime.datetime.now(), posteoId = pk)
        comentario.save()

        return render(request, 'AppDesafio/inicio.html', {'mensaje':' Comentario agregado exitosamente.', 'success':'success','url':avatar[0].avatar.url })

    if avatar:
         return render(request, 'AppDesafio/comentarPost.html', {'posteo': posteo, 'comentarios': comentarios, 'avatarComentario': avatarComentario, 'url':avatar[0].avatar.url})    

    return render(request, 'AppDesafio/comentarPost.html', {'posteo': posteo, 'comentarios': comentarios, 'avatarComentario': avatarComentario})


#---- Login ------

def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request=request, data = request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user=user)                
                return render (request, 'AppDesafio/inicio.html', {'usuario': usuario, 'mensaje': 'Bienvenido al sistema,' + ' ' + request.user.username, 'success':'success','url':avatar[0].avatar.url })
                   
            else:
                return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Datos erróneos.','error':'error' })
        else:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Datos erróneos, intente nuevamente.', 'error':'error' })
    
    else:
        formulario = AuthenticationForm()
        return render (request, 'AppDesafio/login.html', {'formulario': formulario })

def register(request):
     if request.method == "POST":
         formulario = UserRegistrationForm(request.POST)
         if formulario.is_valid():
             username=formulario.cleaned_data['username']
             if formulario.save():
                 user=User.objects.get(username=username)
                 user.groups.add(1)
                 user.save()
                 avatar = Avatar(user=user,avatar= 'avatar/anonymous-user-icon-2.jpg' )
                 avatar.save()
                 return render (request, 'AppDesafio/inicio.html', {'mensaje':f'USUARIO: {username} creado exitosamente.','success':'success', })
         else:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO SE PUDO CREAR EL USUARIO.', 'error':'error' })

     else:
         formulario = UserRegistrationForm()
         return render (request, 'AppDesafio/register.html', {'formulario': formulario })

#----- Perfil -----------
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)

    if request.method=="POST":
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'AppDesafio/inicio.html', {'usuario': usuario, 'mensaje': 'Perfil editado exitosamente.', 'success':'success','url':avatar[0].avatar.url})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'AppDesafio/editarPerfil.html',{'formulario':formulario, 'usuario':usuario.username, 'url':avatar[0].avatar.url})   

 #------ Avatar ----------
@login_required
def agregarAvatar(request):
    
    user=User.objects.get(username=request.user)
    avatar = Avatar.objects.filter(user=request.user)

    if request.method == "POST":
         formulario = AvatarForm(request.POST, request.FILES)
         if formulario.is_valid():

             avatarViejo = Avatar.objects.get(user=request.user)
             if(avatarViejo.avatar):
                avatarViejo.delete()
             avatar = Avatar(user=user,avatar= formulario.cleaned_data['avatar'])
             avatar.save()
             avatar = Avatar.objects.filter(user=request.user)
             return render(request, 'AppDesafio/inicio.html', {'usuario': user , 'mensaje': 'Avatar cambiado exitosamente', 'success':'success', 'url':avatar[0].avatar.url })
    else:
        formulario=AvatarForm()
    return render(request, 'AppDesafio/agregarAvatar.html', {'formulario': formulario, 'usuario': user, 'url':avatar[0].avatar.url})     



def about(request):
        if request.user.is_authenticated:      
           avatar = Avatar.objects.filter(user=request.user)
           return render(request, 'AppDesafio/about.html', {'url':avatar[0].avatar.url} )

        return render(request, 'AppDesafio/about.html')

@login_required
def pages(request):
    avatar = Avatar.objects.filter(user=request.user)
    user = request.user
    #chequeo si el usuario se encuentra en el grupo de usuarios comunes.
    if user.groups.filter(name='Usuarios_Comunes').exists():
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO PERMITIDO.','error':'error', 'url':avatar[0].avatar.url })
    posteos = Posteo.objects.all()
    return render(request, 'AppDesafio/pages.html', {'posteos':posteos, 'url':avatar[0].avatar.url} )

@login_required
def detallePost(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    user = request.user
    #chequeo si el usuario se encuentra en el grupo de usuarios comunes.
    if user.groups.filter(name='Usuarios_Comunes').exists():
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO PERMITIDO.', 'error':'error', 'url':avatar[0].avatar.url })
    #validamos que tenga un objeto, sino error.
    try:
        posteo = Posteo.objects.get(id=pk)
    except:
        return render(request, 'AppDesafio/inicio.html', {'mensaje': 'No hay páginas aún', 'error':'error', 'url':avatar[0].avatar.url} )   

    return render(request, 'AppDesafio/pages.html', {'posteo':posteo, 'url':avatar[0].avatar.url} )   



