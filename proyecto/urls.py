from django.contrib import admin
from django.urls import path, include
from .views import *
from AppDesafio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('AppDesafio/', include('AppDesafio.urls')),
]
