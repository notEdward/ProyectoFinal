import datetime
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from AppDesafio.forms import UserRegistrationForm, UserEditForm
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import os

# Create your views here.

def inicio(request):

    posteos = Item.objects.all()
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
        return render(request, 'AppDesafio/inicio.html', {'posteos': posteos, 'url':avatar[0].avatar.url })

    
    return render(request, 'AppDesafio/inicio.html', {'posteos': posteos})    


    

# def formulario(request):    

#     if request.method == 'POST':
#         persona = Persona(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
#         persona.save()
#         animal = Animal(especie = request.POST['especie'], nombre = request.POST['nombremascota'], fecha_ingreso = datetime.datetime.now())
#         animal.save()
#         donacion = Donacion(monto = request.POST['monto'], nota_donacion = request.POST['nota_donacion']) 
#         donacion.save()

#         return render(request, "AppDesafio/inicio.html")

#     return render(request, "AppDesafio/formulario.html")

# @login_required
# def buscar(request):
#     return render(request, "AppDesafio/buscar.html")      

# def resultados(request):

#     if request.GET['especie']:
#         especie = request.GET['especie']
#         animal = Animal.objects.filter(especie = especie)

#         return render (request, 'AppDesafio/resultados.html', {'animal': animal, 'especie': especie })

#     else:

#         return render (request, 'AppDesafio/resultados.html', {'especie': '' })

#---- Img ----
@login_required
def agregarPost(request):
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
    if request.method == "POST":
        posteo = Item()
        posteo.usuarioCreador = request.user
        posteo.fecha = datetime.datetime.now()
        posteo.titulo = request.POST.get('titulo')
        posteo.descripcion = request.POST.get('descripcion')

        if len(request.FILES) != 0:
            posteo.imagen = request.FILES['imagen']

        posteo.save()
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Posteo creado exitosamente.' })

    return render(request, 'AppDesafio/newPost.html', {'url':avatar[0].avatar.url})        

def editarPost(request, pk):
    if request.user.is_authenticated:      
        avatar = Avatar.objects.filter(user=request.user)
    posteo = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(posteo.imagen) > 0:
                os.remove(posteo.imagen.path)
            posteo.imagen = request.FILES['imagen']
        posteo.titulo = request.POST.get('titulo')
        posteo.descripcion = request.POST.get('descripcion')
        posteo.save()
        return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Posteo editado exitosamente.', 'url':avatar[0].avatar.url })

    return render(request, 'AppDesafio/editPost.html', {'posteo': posteo, 'url':avatar[0].avatar.url})
    



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
                return render (request, 'AppDesafio/inicio.html', {'usuario': usuario, 'mensaje': 'Bienvenido al sistema' })
            else:
                return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Datos erróneos.' })
        else:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'Formulario invalido, intente nuevamente.' })
    
    else:
        formulario = AuthenticationForm()
        return render (request, 'AppDesafio/login.html', {'formulario': formulario })

def register(request):
     if request.method == "POST":
         formulario = UserRegistrationForm(request.POST)
         if formulario.is_valid():
             username=formulario.cleaned_data['username']
             formulario.save()
             return render (request, 'AppDesafio/inicio.html', {'mensaje':f'USUARIO: {username} creado exitosamente.' })
         else:
            return render (request, 'AppDesafio/inicio.html', {'mensaje': 'NO SE PUDO CREAR EL USUARIO.' })

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

            return render(request, 'AppDesafio/inicio.html', {'usuario': usuario, 'mensaje': 'Perfil editado exitosamente.'})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, 'AppDesafio/editarPerfil.html',{'formulario':formulario, 'usuario':usuario.username, 'url':avatar[0].avatar.url})   

            