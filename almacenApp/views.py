from dataclasses import fields
from decimal import Decimal
import json
from multiprocessing import context
import pdb
from pickle import FALSE
from django.core import serializers
from django.shortcuts import render, redirect
from ventasApp.models import DocumentoIdentidad
from .forms import NotaAlmacenForm, OrdenCompraform, ProveedorForm
from .models import DetalleNotaAlmacen, DetalleOrdenCompra, NotaAlmacen, OrdenCompra, Proveedor
from django.core.paginator import Paginator
from django.contrib import messages 

# Create your views here.
#PROVEEDORES
def listarproveedor(request):
    proveedor=Proveedor.objects.filter(eliminado=False)
    paginator = Paginator(proveedor, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"proveedor/listar.html",{'page_obj': page_obj})

def agregarproveedor(request):
    form=ProveedorForm()
    if request.method=="POST":
        form=ProveedorForm(request.POST)
        if form.is_valid():
            nombres_proveedor=form.cleaned_data.get("nombres")
            apellidos_proveedor=form.cleaned_data.get("apellidos")
            direccion_proveedor=form.cleaned_data.get("direccion")
            razonsocial_proveedor=form.cleaned_data.get("razonsocial")
            telefono_proveedor=form.cleaned_data.get("telefono")

            proveedor_exits=(Proveedor.objects.filter(apellidos=apellidos_proveedor).count()>0)
            if proveedor_exits:
                messages.info(request, "Proveedor ya existe")
                return redirect("agregarproveedor")
            else:
                form.save() 
                return redirect("listarproveedor") 
        else:
            form=ProveedorForm()
    context={'form':form} 
    return render(request,"proveedor/agregar.html",context)

def editarproveedor(request,id):
    proveedor=Proveedor.objects.get(codproveedor=id)
    if request.method=="POST":
        form=ProveedorForm(request.POST,instance=proveedor)
        if form.is_valid():
            form.save() 
            return redirect("listarproveedor") 
    else:
        form=ProveedorForm(instance=proveedor)
        context={"form":form} 
        return render(request,"proveedor/editar.html",context)

def eliminarproveedor(request,id):
    proveedor=Proveedor.objects.get(codproveedor=id) 
    proveedor.eliminado = True
    proveedor.save()
    return redirect("listarproveedor") 

#NOTAS ALMACEN
def listarNotasAlmacen(request):
    notasAlmacen = NotaAlmacen.objects.filter(eliminado=False)
    paginator = Paginator(notasAlmacen, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"notasAlmacen/listar.html",{'page_obj': page_obj})

def agregarNotaAlmacen(request):
    form = NotaAlmacenForm()
    if request.method=="POST":
        form = NotaAlmacenForm(request.POST)
        if form.is_valid():
            tipoNota = form.cleaned_data.get('tipoNota')
            fecha = form.cleaned_data.get('fecha')
            trabajador = form.cleaned_data.get('trabajador')
            motivo = form.cleaned_data.get('motivo')
            estado = form.cleaned_data.get('estado')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            detalleNota = form.cleaned_data.get('estado')
            
            # breakpoint()
            
            notaalmacen = NotaAlmacen()
            notaalmacen.tipoNota = tipoNota
            notaalmacen.fecha = fecha
            notaalmacen.codTrabajador = trabajador
            notaalmacen.motivo = motivo
            notaalmacen.estado = estado
            notaalmacen.eliminado = 0
            # breakpoint()
            
            notaalmacen.save()
            
            for detalle in detalleJSON:
                tempDetalle = DetalleNotaAlmacen(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],codNotaAlmacen=notaalmacen, eliminado=0)
                tempDetalle.save()
            breakpoint()
            return redirect('listarNotasAlmacen')    
        else:
            form = NotaAlmacenForm()
    context = {'form':form}
    return render(request,"notasAlmacen/agregar.html",context)        

def editarNotaAlmacen(request,id):
    notaAlmacen = NotaAlmacen.objects.get(codNotaAlmacen=id)
    detalle = DetalleNotaAlmacen.objects.filter(codNotaAlmacen=id).values('codDetalleNota','codNotaAlmacen','descripcion','cantidad','eliminado')
    # strDetalle = serializers.serialize("json",list(detalle),fields={'descripcion'})
    strDetalle = json.dumps([dict(item) for item in detalle])
    if request.method=="POST":
        form=NotaAlmacenForm(request.POST)
        if form.is_valid():
            tipoNota = form.cleaned_data.get('tipoNota')
            fecha = form.cleaned_data.get('fecha')
            trabajador = form.cleaned_data.get('trabajador')
            motivo = form.cleaned_data.get('motivo')
            estado = form.cleaned_data.get('estado')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            detalleNota = form.cleaned_data.get('estado')
            
            # breakpoint()
            
            notaAlmacen.tipoNota = tipoNota
            notaAlmacen.fecha = fecha
            notaAlmacen.codTrabajador = trabajador
            notaAlmacen.motivo = motivo
            notaAlmacen.estado = estado
            notaAlmacen.eliminado = 0
            # breakpoint()
            
            notaAlmacen.save()
            
            for detalle in detalleJSON:
                if(detalle['codDetalleNota']==0):
                    tempDetalle = DetalleNotaAlmacen(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],codNotaAlmacen=notaAlmacen, eliminado=0)
                    tempDetalle.save()
                else:
                    tempDetalle = DetalleNotaAlmacen.objects.get(codDetalleNota=detalle['codDetalleNota'])
                    tempDetalle.descripcion=detalle['descripcion']
                    tempDetalle.cantidad=detalle['cantidad']
                    tempDetalle.eliminado=detalle['eliminado']
                    tempDetalle.save()
            return redirect('listarNotasAlmacen')    
    else:
        
        initial_dic = {
            'tipoNota': notaAlmacen.tipoNota,
            'fecha': notaAlmacen.fecha,
            'motivo': notaAlmacen.motivo,
            'trabajador': notaAlmacen.codTrabajador,
            'estado': notaAlmacen.estado,
            'detalle': strDetalle,
            'codVenta': notaAlmacen.codVenta,
        }
        
        form=NotaAlmacenForm(request.POST or None, initial=initial_dic)
        context={"form":form, "detalle": detalle}
        return render(request, "notasAlmacen/editar.html",context)

def eliminarNotaAlmacen(request,id):
    notaAlmacen = NotaAlmacen.objects.get(codNotaAlmacen=id)
    notaAlmacen.eliminado = True
    notaAlmacen.save()
    return redirect("listarNotasAlmacen")

#ORDENES COMPRA
def listarOrdenesCompra(request):
    ordenesCompra = OrdenCompra.objects.filter(eliminado=False)
    paginator = Paginator(ordenesCompra, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"ordenCompra/listar.html",{'page_obj': page_obj})

def agregarOrdenCompra(request):
    form = OrdenCompraform()
    if request.method=="POST":
        form = OrdenCompraform(request.POST)
        if form.is_valid():
            trabajador = form.cleaned_data.get('trabajador')
            proveedor = form.cleaned_data.get('proveedor')
            igv = form.cleaned_data.get('igv')
            fecha = form.cleaned_data.get('fecha')
            descuento = form.cleaned_data.get('descuento')
            estado = form.cleaned_data.get('estado')
            observaciones = form.cleaned_data.get('observaciones')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            
            # breakpoint()
            
            ordencompra = OrdenCompra()
            ordencompra.codTrabajador = trabajador
            ordencompra.codProveedor = proveedor
            ordencompra.igv = igv
            ordencompra.fecha = fecha
            ordencompra.descuento = descuento
            ordencompra.estado = estado
            ordencompra.observaciones = observaciones
            ordencompra.eliminado = 0
            # breakpoint()
            
            ordencompra.save()
            
            for detalle in detalleJSON:
                tempDetalle = DetalleOrdenCompra(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],precioUnitario=detalle['precio'],codMaterial=None,codProductoProveedor=None,codOrdenCompra=ordencompra, eliminado=0)
                tempDetalle.save()
            breakpoint()
            return redirect('listarOrdenesCompra')    
        else:
            form = OrdenCompraform()
    context = {'form':form}
    return render(request,"ordencompra/agregar.html",context)     

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

def editarOrdenCompra(request,id):
    ordenCompra = OrdenCompra.objects.get(codOrdenCompra=id)
    detalle = DetalleOrdenCompra.objects.filter(codOrdenCompra=id).values('codDetalleOrdenCompra','codOrdenCompra','descripcion','cantidad','eliminado','precioUnitario')
    # strDetalle = serializers.serialize("json",list(detalle),fields={'descripcion'})
    strDetalle = json.dumps([dict(item) for item in detalle], cls=DecimalEncoder)
    if request.method=="POST":
        form=OrdenCompraform(request.POST)
        if form.is_valid():
            codTrabajador = form.cleaned_data.get('trabajador')
            codProveedor = form.cleaned_data.get('proveedor')
            fecha = form.cleaned_data.get('fecha')
            estado = form.cleaned_data.get('estado')
            igv = form.cleaned_data.get('igv')
            descuento = form.cleaned_data.get('descuento')
            observaciones = form.cleaned_data.get('observaciones')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            
            # breakpoint()
            
            ordenCompra.codTrabajador = codTrabajador
            ordenCompra.codProveedor = codProveedor
            ordenCompra.fecha = fecha
            ordenCompra.estado = estado
            ordenCompra.igv = igv
            ordenCompra.descuento = descuento
            ordenCompra.observaciones = observaciones
            ordenCompra.eliminado = 0
            # breakpoint()
            
            ordenCompra.save()
            
            for detalle in detalleJSON:
                if(detalle['codDetalleOrdenCompra']==0):
                    tempDetalle = DetalleOrdenCompra(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],precioUnitario=detalle['precio'],codOrdenCompra=ordenCompra,codMaterial=None,codProductoProveedor=None, eliminado=0)
                    tempDetalle.save()
                else:
                    tempDetalle = DetalleOrdenCompra.objects.get(codDetalleOrdenCompra=detalle['codDetalleOrdenCompra'])
                    tempDetalle.descripcion=detalle['descripcion']
                    tempDetalle.cantidad=detalle['cantidad']
                    tempDetalle.precioUnitario=detalle['precio']
                    # tempDetalle.codMaterial= detalle['codMaterial'] or None
                    # tempDetalle.codProductoProveedor= detalle['codProductoProveedor'] or None
                    tempDetalle.eliminado=detalle['eliminado']
                    tempDetalle.save()
            return redirect('listarOrdenesCompra')    
    else:
        
        initial_dic = {
            'trabajador': ordenCompra.codTrabajador,
            'proveedor': ordenCompra.codProveedor,
            'igv': ordenCompra.igv,
            'fecha': ordenCompra.fecha,
            'descuento': ordenCompra.descuento,
            'estado': ordenCompra.estado,
            'observaciones': ordenCompra.observaciones,
            'detalle': strDetalle,
        }
        
        form=OrdenCompraform(request.POST or None, initial=initial_dic)
        context={"form":form, "detalle": detalle}
        return render(request, "ordenCompra/editar.html",context)

def eliminarOrdenCompra(request,id):
    ordencompra = OrdenCompra.objects.get(codOrdenCompra=id)
    ordencompra.eliminado = True
    ordencompra.save()
    return redirect("listarOrdenesCompra")













