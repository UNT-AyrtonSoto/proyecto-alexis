from pyexpat import model
from tkinter import HIDDEN
from django import forms 
from django.forms import fields
from produccionApp.models import Trabajador 
from ventasApp.models import DocumentoIdentidad
from .models import EstadoNota, MotivoNota, NotaAlmacen, Proveedor

#Trabajador
class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=['nombres','apellidos','direccion','razonSocial','telefono','nroDocumento','codDocumentoIdentidad'] 
        
class NotaAlmacenForm(forms.Form):
    tipoNota = forms.ChoiceField(choices=(('E','ENTRADA'),('S','SALIDA')))
    fecha=forms.DateField()
    detalle=forms.CharField(widget=forms.HiddenInput(), required=False)
    # detalleNota=forms.CharField()
    trabajador=forms.ModelChoiceField(queryset=Trabajador.objects.all())
    motivo=forms.ModelChoiceField(queryset=MotivoNota.objects.all())
    estado=forms.ModelChoiceField(queryset=EstadoNota.objects.all())
    # class Meta:
    #     model = NotaAlmacen
    #     fields = ['tipoNota','fecha','trabajador','motivo','estado','codVenta','detalle']
    