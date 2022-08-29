from django.contrib import admin

# Register your models here.
from .models import Banco, EstadoPedido, Moneda, CuentaBancaria, Cliente, DocumentoIdentidad

class BancoAdmin(admin.ModelAdmin):
    list_display= ("idBanco","nombre")

class MonedaAdmin(admin.ModelAdmin):
    list_display= ("idMoneda","descripcion")
    
class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display= ("nroCuenta","tipoCuenta","idBanco","idMoneda")
    
class ClientesAdmin(admin.ModelAdmin): 
    list_display=("nombres","apellidos","direccion","celular","edad","fechaNacimiento","nroDocumento","codDocumentoIdentidad","razonSocial")
    
class MonedaAdmin(admin.ModelAdmin):
    list_display= ("idMoneda","descripcion")
    
class DocumentoIdentidadAdmin(admin.ModelAdmin):
    list_display=("codDocumentoIdentidad","descripcion")
 
admin.site.register(Banco)
admin.site.register(Moneda)
admin.site.register(CuentaBancaria)
admin.site.register(Cliente)   
admin.site.register(DocumentoIdentidad)
admin.site.register(EstadoPedido)