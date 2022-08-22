from django import forms 
from .models import Rol, Usuario

class RolForm(forms.ModelForm):
    class Meta:
        model=Rol
        fields=['rol','descripcion']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre',
                'dni' ,
                'apellidoPaterno', 
                'apellidoMaterno', 
                'direccion', 
                'correo', 
                'celular', 
                'rol']

