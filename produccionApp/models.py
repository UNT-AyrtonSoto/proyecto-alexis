from django.db import models

# Create your models here.  
class Trabajador (models.Model): 
    codTrabajador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    correo = models.EmailField(max_length=100)
    fechaContratos= models.DateField(auto_now_add=True)
    nroDocumento = models.CharField(max_length=20)
    codDocumentoIdentidad = models.ForeignKey('ventasApp.DocumentoIdentidad', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)
