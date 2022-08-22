from django.contrib import admin
from .models import EstadoNota, MotivoNota, Proveedor
# Register your models here.
admin.site.register(Proveedor)
admin.site.register(MotivoNota)
admin.site.register(EstadoNota)