from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codproveedor=models.AutoField(primary_key=True)
    nombres= models.CharField(max_length=40)
    apellidos= models.CharField(max_length=40)
    direccion= models.CharField(max_length=50)
    razonSocial= models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    nroDocumento = models.CharField(max_length=15)
    codDocumentoIdentidad = models.ForeignKey('ventasApp.DocumentoIdentidad', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)