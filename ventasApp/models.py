from pickle import TRUE
from xml.etree.ElementTree import tostring
from django.db import models

# Create your models here.
class DocumentoIdentidad(models.Model):
    codDocumentoIdentidad=models.CharField(max_length=8, primary_key=TRUE)
    descripcion=models.CharField(max_length=40)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.descripcion
    
class Banco(models.Model):
    idBanco=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.nombre

class Moneda(models.Model):
    idMoneda=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=50)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.descripcion

class CuentaBancaria(models.Model):
    nroCuenta=models.CharField(primary_key=True, max_length=25)
    tipoCuenta=models.CharField(max_length=20)
    idBanco=models.ForeignKey(Banco,on_delete=models.CASCADE)
    idMoneda=models.ForeignKey(Moneda,on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Cliente(models.Model):
    codCliente=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=100)
    correo=models.EmailField()
    direccion=models.CharField(max_length=150)
    celular=models.CharField(max_length=8)
    edad=models.IntegerField()
    fechaNacimiento=models.DateField()
    nroDocumento=models.CharField(max_length=20)
    codDocumentoIdentidad = models.ForeignKey('DocumentoIdentidad', on_delete=models.CASCADE)
    razonSocial=models.CharField(max_length=30)    
    eliminado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombres + ' ' + self.apellidos

class EstadoPedido(models.Model):
    codEstadoPedido=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=25)
    eliminado=models.BooleanField(default=False)

class Pedido(models.Model):
    codPedido=models.AutoField(primary_key=True)
    fechaEntrega=models.DateField()
    estado=models.ForeignKey('EstadoPedido',on_delete=models.CASCADE)
    documentoCliente = models.CharField(max_length=15)
    nombreCliente = models.CharField(max_length= 75)
    activo = models.BooleanField(default=True)
    eliminado=models.BooleanField(default=False)
    
class DetallePedido(models.Model):
    codDetallePedido = models.AutoField(primary_key=True)
    codPedido = models.ForeignKey('Pedido',on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=35)
    cantidad = models.IntegerField()
    eliminado=models.BooleanField(default=False)
