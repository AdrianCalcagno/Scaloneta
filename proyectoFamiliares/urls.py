from django.contrib import admin
from django.urls import path
from appFamiliares.views import integrantes, contacto, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('integrantes/', integrantes, name="integrantes"),
    path('contacto/', contacto, name="contacto"),
    path('', inicio, name="inicio"),
]
