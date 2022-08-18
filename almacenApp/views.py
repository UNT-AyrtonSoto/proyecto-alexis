from django.shortcuts import render, redirect
from .forms import ProveedorForm
from .models import Proveedor
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