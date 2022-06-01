from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola mundo")