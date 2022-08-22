from django.contrib import admin
from .models import IGV, EstadoNota, EstadoOrdenCompra, MotivoNota, Proveedor
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(MotivoNota)
admin.site.register(EstadoNota)
admin.site.register(EstadoOrdenCompra)
admin.site.register(IGV)