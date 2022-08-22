from pickle import TRUE
from xmlrpc.client import Boolean
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codproveedor=models.AutoField(primary_key=True)
    nombres= models.CharField(max_length=40)
    apellidos= models.CharField(max_length=40)
    direccion= models.CharField(max_length=50)
    razonSocial= models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    nroDocumento = models.CharField(max_length=15, unique=TRUE)
    codDocumentoIdentidad = models.ForeignKey('ventasApp.DocumentoIdentidad', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

class MotivoNota(models.Model):
    codMotivoNota=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado=models.BooleanField()
    
    def __str__(self) -> str:
        return self.descripcion
    
class EstadoNota(models.Model):
    codEstadoNota=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado=models.BooleanField()
    
    def __str__(self) -> str:
        return self.descripcion

class NotaAlmacen(models.Model):
    codNotaAlmacen=models.AutoField(primary_key=True)
    tipoNota=models.CharField(max_length=1)
    fecha=models.DateField()
    codTrabajador=models.ForeignKey('produccionApp.Trabajador',on_delete=models.CASCADE)
    motivo=models.ForeignKey('MotivoNota',on_delete=models.CASCADE)
    estado=models.ForeignKey('EstadoNota',on_delete=models.CASCADE)
    codVenta=models.IntegerField(null=True)
    # codVenta=models.ForeignKey('ventasApp.PedidoVenta',on_delete=models.CASCADE,null=TRUE)
    eliminado=models.BooleanField()

class DetalleNotaAlmacen(models.Model):
    codDetalleNota=models.AutoField(primary_key=True)
    codNotaAlmacen=models.ForeignKey('NotaAlmacen',on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    eliminado=models.BooleanField()