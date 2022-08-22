import json
from multiprocessing import context
import pdb
from django.core import serializers
from django.shortcuts import render, redirect
from ventasApp.models import DocumentoIdentidad
from .forms import NotaAlmacenForm, ProveedorForm
from .models import DetalleNotaAlmacen, NotaAlmacen, Proveedor
from django.core.paginator import Paginator
from django.contrib import messages 

# Create your views here.
#PROVEEDORES
def listarproveedor(request):
    proveedor=Proveedor.objects.all()
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
    proveedor.save()
    return redirect("listarproveedor") 

#NOTAS ALMACEN
def listarNotasAlmacen(request):
    notasAlmacen = NotaAlmacen.objects.all()
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
    detalle = DetalleNotaAlmacen.objects.filter(codNotaAlmacen=id)
    strDetalle = serializers.serialize("json",detalle)
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
                if(detalle.idDetalle==0):
                    tempDetalle = DetalleNotaAlmacen(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],codNotaAlmacen=notaAlmacen, eliminado=0)
                    tempDetalle.save()
                    breakpoint()
                else:
                    tempDetalle = DetalleNotaAlmacen.objects.get(codDetalleNota=detalle['idDetalle'])
                    tempDetalle.descripcion=detalle['descripcion']
                    tempDetalle.cantidad=detalle['cantidad']
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
    pass















