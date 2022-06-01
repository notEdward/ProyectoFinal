import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    return render(request, "AppDesafio/inicio.html")

def formulario(request):    

    if request.method == 'POST':
        persona = Persona(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        persona.save()
        animal = Animal(especie = request.POST['especie'], nombre = request.POST['nombremascota'], fecha_ingreso = datetime.datetime.now())
        animal.save()
        donacion = Donacion(monto = request.POST['monto'], nota_donacion = request.POST['nota_donacion']) 
        donacion.save()

        return render(request, "AppDesafio/inicio.html")

    return render(request, "AppDesafio/formulario.html")

def buscar(request):
    return render(request, "AppDesafio/buscar.html")      

def resultados(request):

    if request.GET['especie']:
        especie = request.GET['especie']
        animal = Animal.objects.filter(especie = especie)

        return render (request, 'AppDesafio/resultados.html', {'animal': animal, 'especie': especie })

    else:

        return render (request, 'AppDesafio/resultados.html', {'especie': '' })