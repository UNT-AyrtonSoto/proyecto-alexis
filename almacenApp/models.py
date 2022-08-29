from pickle import TRUE
from statistics import mode
from turtle import ondrag
from xmlrpc.client import Boolean
from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codproveedor=models.AutoField(primary_key=True)
    nombres= models.CharField(max_length=40, null= True)
    apellidos= models.CharField(max_length=40, null= True)
    direccion= models.CharField(max_length=50)
    razonSocial= models.CharField(max_length=100, null= True)
    telefono=models.CharField(max_length=8)
    nroDocumento = models.CharField(max_length=15, unique=TRUE)
    codDocumentoIdentidad = models.ForeignKey('ventasApp.DocumentoIdentidad', on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.razonSocial

class MotivoNota(models.Model):
    codMotivoNota=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.descripcion
    
class EstadoNota(models.Model):
    codEstadoNota=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.descripcion

class EstadoOrdenCompra(models.Model):
    codEstadoOrdenCompra= models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.descripcion
    
class IGV(models.Model):
    anio=models.IntegerField(primary_key=True)
    porcentaje=models.DecimalField(decimal_places=2,max_digits=8)
    activo=models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f"{self.anio} ({self.porcentaje*100}%)"
class NotaAlmacen(models.Model):
    codNotaAlmacen=models.AutoField(primary_key=True)
    tipoNota=models.CharField(max_length=1)
    fecha=models.DateField()
    codTrabajador=models.ForeignKey('produccionApp.Trabajador',on_delete=models.CASCADE)
    motivo=models.ForeignKey('MotivoNota',on_delete=models.CASCADE)
    estado=models.ForeignKey('EstadoNota',on_delete=models.CASCADE)
    codVenta=models.IntegerField(null=True)
    # codVenta=models.ForeignKey('ventasApp.PedidoVenta',on_delete=models.CASCADE,null=TRUE)
    eliminado = models.BooleanField(default=False)

class DetalleNotaAlmacen(models.Model):
    codDetalleNota=models.AutoField(primary_key=True)
    codNotaAlmacen=models.ForeignKey('NotaAlmacen',on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    eliminado = models.BooleanField(default=False)
    
class OrdenCompra(models.Model):
    codOrdenCompra=models.AutoField(primary_key=True)
    codTrabajador=models.ForeignKey('produccionApp.Trabajador',on_delete=models.CASCADE)
    codProveedor=models.ForeignKey('Proveedor',on_delete=models.CASCADE)
    fecha=models.DateField()
    estado=models.ForeignKey('EstadoOrdenCompra',on_delete=models.CASCADE)
    igv=models.ForeignKey('IGV', on_delete=models.CASCADE)
    descuento=models.DecimalField(null=True,decimal_places=2,max_digits=8)
    observaciones=models.TextField(null=True)
    eliminado=models.BooleanField(default=False)
    
class DetalleOrdenCompra(models.Model):
    codDetalleOrdenCompra=models.AutoField(primary_key=True)
    codOrdenCompra=models.ForeignKey('OrdenCompra',on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=30)
    cantidad=models.IntegerField()
    precioUnitario=models.DecimalField(decimal_places=2, max_digits=8)
    codMaterial=models.IntegerField(null=True)
    codProductoProveedor=models.IntegerField(null=True)
    eliminado=models.BooleanField(default=False)