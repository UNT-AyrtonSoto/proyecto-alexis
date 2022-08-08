from django.db import models

# Create your models here.
class Documento_Identidad(models.Model):
    coddocumentoidentidad=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=40)

class Proveedor(models.Model):
    codproveedor=models.AutoField(primary_key=True)
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    direccion=models.CharField(max_length=50)
    razonsocial=models.CharField(max_length=100)
    telefono=models.CharField(max_length=8)
    nrodocumento=models.CharField(max_length=5)
    coddocumentoidentidad=models.ForeignKey(Documento_Identidad,on_delete=models.CASCADE)
    
