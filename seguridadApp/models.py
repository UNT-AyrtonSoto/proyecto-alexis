from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Rol(models.Model):
    idRol=models.AutoField(primary_key=True)
    rol=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.rol

# class Usuario(models.Model):
#     idUsuario=models.AutoField(primary_key=True)
#     nombre=models.CharField(max_length=50)
#     dni=models.CharField(max_length=9)
#     apellidoPaterno = models.CharField(max_length=100)
#     apellidoMaterno = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=150)
#     correo = models.EmailField(max_length=100)
#     celular=models.IntegerField()
#     rol=models.ForeignKey('seguridadApp.Rol', on_delete=models.CASCADE)
#     eliminado = models.BooleanField(default=False)
    
#     def __str__(self) -> str:
#         return self.dni

class Usuario(AbstractUser):
    nombre=models.CharField(max_length=50 , default='')
    dni=models.CharField(max_length=8 , default='')
    apellidoPaterno = models.CharField(max_length=100, default='')
    apellidoMaterno = models.CharField(max_length=100, default='')
    direccion = models.CharField(max_length=150 , default='')
    celular=models.CharField(max_length=9, default='')
    rol=models.ForeignKey('seguridadApp.Rol', on_delete=models.CASCADE, default=1)
    eliminado = models.BooleanField(default=False)
    class Meta:
        db_table = 'auth_user'
        
    # username = models.CharField(max_length=255, unique=True, default="Some String")
