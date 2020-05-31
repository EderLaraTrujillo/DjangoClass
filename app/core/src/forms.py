from django import forms
from .pqrsf import pqrsf

# Creamos las clases con los formularios pertinentes:
class ContactForm(forms.Form):
    # Atributos del formulario de contacto:
    tipomsj =  forms.ChoiceField(label="Tipo de Petición", required=True, choices=pqrsf, widget=forms.Select(attrs={'class':'form-control'}))
    usuario = forms.CharField(label="Tu Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre Completo'}))
    correo = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escribe tu Correo Electrónico'}))
    mensaje = forms.CharField(label="Mensaje", required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Escribe tu Mensaje'}))