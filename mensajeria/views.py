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

from AppDesafio.forms import AvatarForm

# Create your views here.
@login_required
def mensajeria(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    usuarios = User.objects.all()
    mensajes = Mensaje.objects.filter(destinatario_id=request.user.id)

    return render(request, 'mensajeria/mensajeria.html',  {'usuarios': usuarios, 'mensajes': mensajes, 'url':avatar[0].avatar.url })