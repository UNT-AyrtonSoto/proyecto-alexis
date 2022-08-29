from django import forms 
from .models import Rol, Usuario
from django.contrib.auth.forms import UserCreationForm

class RolForm(forms.ModelForm):
    class Meta:
        model=Rol
        fields=['rol','descripcion']

class UsuarioForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=['nombre',
                'dni' ,
                'apellidoPaterno', 
                'apellidoMaterno', 
                'direccion', 
                'email',
                'celular', 
                'rol',
                'username',
                'password1',
                'password2']

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['direccion'].required = False
        self.fields['celular'].required = False
        self.fields['email'].required = True


class DatosPersonalesForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=['nombre',
                'dni' ,
                'apellidoPaterno', 
                'apellidoMaterno', 
                'direccion', 
                'email',
                'celular']

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['direccion'].required = False
        self.fields['celular'].required = False
        self.fields['email'].required = True

class PasswordForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=[
                'password1',
                'password2']
