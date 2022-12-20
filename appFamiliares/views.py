from django.shortcuts import render
from .models import Jugadores, Mensajes, Copas
from django.http import HttpResponse

def inicio(request):
    return render (request, "appFamiliares/padre.html")

def integrantes(request):
    return render (request, "appFamiliares/integrantes.html")

def contacto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        asunto = request.POST["asunto"]
        mensaje = request.POST["mensaje"]
        final = Mensajes(nombre=nombre, email=email, asunto=asunto, mensaje=mensaje)
        final.save()
        return render (request, "appFamiliares/contacto.html", {"mensaje":"Mensaje enviado"})
    else:
        return render (request, "appFamiliares/contacto.html")


