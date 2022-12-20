from django import forms

class MensajesForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    email = forms.EmailField(label="Email")
    asunto = forms.CharField(label="Asunto", max_length=200)
    mensaje = forms.CharField(label="Mensaje", max_length=200)