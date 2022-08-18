from django import forms 
from django.forms import fields 
from .models import Banco, Moneda, CuentaBancaria, Cliente, DocumentoIdentidad

class BancoForm(forms.ModelForm):
    class Meta:
        model=Banco
        fields=['nombre','pais']
        
class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model= CuentaBancaria
        fields=['nroCuenta','tipoCuenta','idBanco','idMoneda','activo']

class MonedaForm(forms.ModelForm):
    class Meta:
        model=Moneda
        fields=['descripcion']

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres',
                'apellidos',
                'correo',
                'direccion',
                'celular',
                'edad',
                'fechaNacimiento',
                'nroDocumento',
                'codDocumentoIdentidad',
                'razonSocial']

class DocumentoIdentidadForms(forms.ModelForm):
    class Meta:
        model=DocumentoIdentidad
        fields=['codDocumentoIdentidad','descripcion']
