from django import forms 
from django.forms import fields 
from .models import Trabajador

#Trabajador
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model=Trabajador
        fields=['codTrabajador','nombre','apellidos','direccion','correo','nroDocumento','codDocumentoIdentidad','activo']