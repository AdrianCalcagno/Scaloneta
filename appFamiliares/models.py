from django.db import models

class Jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    edad = models.IntegerField()
class Mensajes(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.CharField(max_length=200)
class Copas(models.Model):
    nombre = models.CharField(max_length=50)
    fechadecampeon = models.DateField()
    ultimorival = models.CharField(max_length=50)