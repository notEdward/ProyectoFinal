from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2')
        help_texts={k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Mail")
    password1 = forms.CharField(required=False, label="Modificar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(required=False, label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField(required=False, label="Modificar Apellido")
    first_name = forms.CharField(required=False, label="Modificar Nombre")
    
    class Meta:
        model = User
        fields=('username', 'email', 'password1', 'password2', 'last_name', 'first_name')
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField(label="Avatar")