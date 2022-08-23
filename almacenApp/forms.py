from pyexpat import model
from tkinter import HIDDEN
from django import forms 
from django.forms import fields
from produccionApp.models import Trabajador 
from ventasApp.models import DocumentoIdentidad
from .models import IGV, EstadoNota, EstadoOrdenCompra, MotivoNota, NotaAlmacen, Proveedor

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
    codVenta = forms.IntegerField(required=False)
    # class Meta:
    #     model = NotaAlmacen
    #     fields = ['tipoNota','fecha','trabajador','motivo','estado','codVenta','detalle']
    
class OrdenCompraform(forms.Form):
    trabajador=forms.ModelChoiceField(queryset=Trabajador.objects.all())
    proveedor=forms.ModelChoiceField(queryset=Proveedor.objects.all())
    igv=forms.ModelChoiceField(queryset=IGV.objects.all())
    fecha=forms.DateField()
    descuento = forms.DecimalField(decimal_places=2,max_digits=8)
    estado = forms.ModelChoiceField(queryset=EstadoOrdenCompra.objects.all())
    observaciones = forms.CharField(required=False)
    detalle=forms.CharField(widget=forms.HiddenInput(), required=False)