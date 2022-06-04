from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

path('mensajeria', mensajeria, name="mensajeria"),


]

