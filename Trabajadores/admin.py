import site
from django.contrib import admin

from Trabajadores.models import DOCUMENTO_IDENTIDAD, Trabajador

admin.site.register(Trabajador)

admin.site.register(DOCUMENTO_IDENTIDAD)
# Register your models here.
