from django import forms 
from django.forms import fields 
from ventasApp.models import DocumentoIdentidad
from .models import Proveedor

#Trabajador
class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=['nombres','apellidos','direccion','razonSocial','telefono','nroDocumento','codDocumentoIdentidad'] 