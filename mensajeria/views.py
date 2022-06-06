import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from AppDesafio.forms import UserRegistrationForm, UserEditForm, AvatarForm
from AppDesafio.models import *
from mensajeria.models import *
from django.views.generic import ListView
from AppDesafio.forms import AvatarForm


# Create your views here.
@login_required
def mensajeria(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    usuarios = User.objects.all()
    mensajes = Mensaje.objects.filter(destinatario_id=request.user.id)

    return render(request, 'mensajeria/mensajeria.html',  {'usuarios': usuarios, 'mensajes': mensajes, 'url':avatar[0].avatar.url })


#Enviar mensaje
@login_required
def enviarMensaje(request, pk=None):
    avatar = Avatar.objects.filter(user=request.user)
    #si llega el id por parámetro, envio el usuario y lo cargo en el destinatario.
    if pk:
        destinatario_user = User.objects.get(id=pk)
        if destinatario_user:
            return render(request, 'mensajeria/enviarMensaje.html',  {'destinatario_user': destinatario_user.username, 'url':avatar[0].avatar.url })
    if request.method == 'POST':
        try:
          destinatario = User.objects.get(username=request.POST['destinatario'])
        except:
          return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Usuario no válido, intente nuevamente.', 'error':'error', 'url':avatar[0].avatar.url  })
        if destinatario:
            mensaje = Mensaje(remitente_id= request.user.id, remitente_usuario = request.user, destinatario_id = destinatario.id, destinatario_usuario = destinatario.username,  mensaje = request.POST['mensaje'], fecha = datetime.datetime.now(), visto= 'N')
            mensaje.save()
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Mensaje enviado.','success':'success', 'url':avatar[0].avatar.url})
        else:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Usuario no válido, intente nuevamente.', 'error':'error', 'url':avatar[0].avatar.url  })

    return render(request, 'mensajeria/enviarMensaje.html',  {'url':avatar[0].avatar.url })

@login_required
def verEnviados(request):
    avatar = Avatar.objects.filter(user=request.user)  
    mensajes = Mensaje.objects.filter(remitente_id=request.user.id)

    return render(request, 'mensajeria/verEnviados.html',  {'mensajes': mensajes, 'url':avatar[0].avatar.url })

@login_required
def verNoLeidos(request):
    avatar = Avatar.objects.filter(user=request.user)  
    mensajes = Mensaje.objects.filter(destinatario_id=request.user.id, visto='N')
    return render(request, 'mensajeria/verNoLeidos.html',  {'mensajes': mensajes, 'url':avatar[0].avatar.url })

@login_required
def marcarLeido(request, pk):
    avatar = Avatar.objects.filter(user=request.user)
    mensaje = Mensaje.objects.get(id=pk)
    mensaje.visto = 'S'
    mensaje.save()

    return HttpResponseRedirect('/mensajeria')

@login_required
def nuevoAnuncio(request):
    user = request.user
    avatar = Avatar.objects.filter(user=request.user)

    if user.groups.filter(name='Usuarios_Comunes').exists():
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO PERMITIDO.', 'error':'error', 'url':avatar[0].avatar.url })

    if request.method == 'POST':    
        anuncio = Anuncio()
        anuncio.creador_id = request.user.id
        anuncio.fecha = datetime.datetime.now()
        anuncio.mensaje = request.POST.get('anuncio')
        try:
            anuncio.save()
        except:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Se ha producido un error.', 'error': 'error', 'url':avatar[0].avatar.url })   

        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Anuncio simple creado exitosamente.', 'success':'success', 'url':avatar[0].avatar.url })    

    return render(request, 'mensajeria/nuevoAnuncio.html',  {'url':avatar[0].avatar.url })

@login_required
def verAnuncios(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    anuncios = Anuncio.objects.all()
    return render(request, 'mensajeria/anuncios.html', {'anuncios':anuncios,'url':avatar[0].avatar.url })  

# class AnunciosList(ListView):
    
#     model = Anuncio
#     template_name = 'mensajeria/anuncios.html'

class UsuariosList(ListView):
    
    model = User
    template_name = 'mensajeria/usuarios.html'
