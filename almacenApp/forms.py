from django import forms 
from django.forms import fields 
from .models import Proveedor

#Trabajador
class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=['nombres','apellidos','direccion','razonsocial','telefono','nrodocumento','coddocumentoidentidad'] 