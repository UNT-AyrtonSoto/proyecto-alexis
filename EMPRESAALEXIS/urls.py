"""EMPRESAALEXIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from InicioDashboard.views import bienvenido,index, listarBanco, listarMoneda, agregarBanco, agregarMoneda,listarcliente,agregarcliente,editarcliente,listarproveedor,bienvenido,index,agregarproveedor,editarproveedor,eliminarproveedor
from django.contrib.auth import views
from Trabajadores.views import agregarTrabajador, editarTrabajador, eliminarTrabajador, listarTrabajador



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    path('bienvenido/',bienvenido ,name="bienvenido"), 
    path('bancos/',listarBanco,name="listarBanco"), 
    path('bancos/add',agregarBanco,name="agregarBanco"), 
    path('monedas/',listarMoneda,name="listarMoneda"), 
    path('monedas/add',agregarMoneda,name="agregarMoneda"), 
    path('listarcliente/',listarcliente,name="listarcliente"),
    path('agregarcliente/',agregarcliente,name="agregarcliente"),
    path('editarcliente/<int:id>/',editarcliente,name="editarcliente"),
# TRABAJADORES
    path('listaTrabajador/',listarTrabajador,name="listarTrabajador"),
    path('agregarTrabajador/',agregarTrabajador,name="agregarTrabajador"),
    path('editarTrabajador/<int:id>/',editarTrabajador,name="editarTrabajador"),
    path('eliminarTrabajador/<int:id>/',eliminarTrabajador,name="eliminarTrabajador"),   
#PROVEEDORES
    path('listarproveedor/',listarproveedor,name="listarproveedor"), 
    path('agregarproveedor/',agregarproveedor,name="agregarproveedor"), 
    path('editarproveedor/<int:id>/',editarproveedor,name="editarproveedor"), 
    path('eliminarproveedor/<int:id>/',eliminarproveedor,name="eliminarproveedor"), 
]

