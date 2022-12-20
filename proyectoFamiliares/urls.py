from django.contrib import admin
from django.urls import path
from appFamiliares.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('integrantes/', integrantes, name="integrantes"),
    path('contacto/', contacto, name="contacto"),
    path('', inicio, name="inicio"),
    path('busquedaMensajes/', busquedaMensajes, name="busquedaMensajes"),
    path("buscar/", buscar, name="buscar"),
]
