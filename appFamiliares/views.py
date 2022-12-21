from django.shortcuts import render
from .models import Jugadores, Mensajes, Copas
from django.http import HttpResponse
from appFamiliares.forms import MensajesForm

def inicio(request):
    return render (request, "appFamiliares/padre.html")

def integrantes(request):
    return render (request, "appFamiliares/integrantes.html")

""" def contacto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]
        final = Mensajes(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
        final.save()
        return render (request, "appFamiliares/contacto.html", {"mensaje":"Mensaje enviado"})
    else:
        return render (request, "appFamiliares/contacto.html") """

def contacto(request):
    if request.method == "POST":
        forms = MensajesForm(request.POST)
        if forms.is_valid():
            informacion = forms.cleaned_data
            nombre = informacion["nombre"]
            email = informacion["email"]
            asunto = informacion["asunto"]
            mensaje = informacion["mensaje"]
            final = Mensajes(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
            final.save()
            return render (request, "appFamiliares/padre.html", {"mensaje":"¡Mensaje Enviado! QUE VIVA EL FUTBOL"})
        else:
            return render (request, "appFamiliares/contacto.html", {"forms":forms, "mensaje":"Algo falló, revisá la información"})
    else:
        formulario = MensajesForm()
        return render (request, "appFamiliares/contacto.html", {"forms":formulario})

def busquedaMensajes(request):
    return render (request, "appFamiliares/busquedaMensajes.html")

def buscar(request):
        email = request.GET["email"]
        if email != "":
            mensajes= Mensajes.objects.filter(email__icontains=email)
            return render(request, "appFamiliares/resultadosBusqueda.html", {"mensajes":mensajes})
        else:
            return render(request, "appFamiliares/busquedaMensajes.html", {"mensajes":"Ingresa un email para buscar, por favor"})