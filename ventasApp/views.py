import pdb
from django.shortcuts import render, redirect
from .forms import BancoForm, MonedaForm, ClienteForm
from .models import Banco, Moneda, Cliente
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages 

# Create your views here.
def agregarBanco(request):
    if request.method == "POST":
        form=BancoForm(request.POST)
        if form.is_valid():
            nombre_banco = form.cleaned_data.get('nombre')
            # pais_banco = form.cleaned_data.get('pais')
            banco_exists = (Banco.objects.filter(nombre=nombre_banco).count()>0)
            if(banco_exists):
                messages.info(request, "Banco: "+nombre_banco+", ya se encuentra registrado.")
                form=BancoForm()
                context={'form':form}
                # breakpoint()
                return render(request,"banco/agregar.html",context) 
            else:
                form.save() 
                # breakpoint()
                return redirect("listarBanco")           
    form=BancoForm()
    context={'form':form}
    # breakpoint()
    return render(request,"banco/agregar.html",context) 

def listarBanco(request):
    bancos = Banco.objects.all()
    paginator = Paginator(bancos, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"banco/listar.html",{'page_obj': page_obj})

def agregarMoneda(request):
    if request.method == "POST":
        form=MonedaForm(request.POST)
        if form.is_valid():
            descripcion_moneda = form.cleaned_data.get('descripcion')
            # pais_banco = form.cleaned_data.get('pais')
            moneda_exists = (Moneda.objects.filter(descripcion=descripcion_moneda).count()>0)
            if(moneda_exists):
                messages.info(request, "Moneda: "+descripcion_moneda+", ya se encuentra registrado.")
                form=MonedaForm()
                context={'form':form}
                return render(request,"moneda/agregar.html",context) 
            else:
                form.save() 
                return redirect("listarMoneda")     
    form=MonedaForm()
    context={'form':form}
    return render(request,"moneda/agregar.html",context)         
            

def listarMoneda(request):
    monedas = Moneda.objects.all()
    paginator = Paginator(monedas, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"moneda/listar.html",{'page_obj': page_obj})

def agregarcliente(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            nrodocumento_cliente = form.cleaned_data.get("nroDocumento")
            cliente_exits = (Cliente.objects.filter(nroDocumento=nrodocumento_cliente).count()>0)
            if cliente_exits:
                messages.info(request, "Cliente ya existe.")
                form=ClienteForm()
                context={'form':form}
                return render(request,"cliente/agregar.html",context) 
            else:
                form.save() 
                return redirect("listarcliente") 

    else:
        form=ClienteForm()
        context={'form':form} 
        return render(request,"cliente/agregar.html",context) 

def listarcliente(request):
 
    queryset = request.GET.get("buscar")
    cliente = Cliente.objects.all().values()
    if queryset:
        cliente=Cliente.objects.filter(Q(nroDocumento__icontains=queryset)).values() 

    paginator = Paginator(cliente, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'cliente':cliente}
    # breakpoint()
    return render(request,"cliente/listar.html",{'page_obj': page_obj})

def editarcliente(request,id):
    cliente=Cliente.objects.get(codCliente=id)
    if request.method=="POST":
        form=ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save() 
            return redirect("listarcliente") 
    else:
        form=ClienteForm(instance=cliente)
        context={"form":form} 
        return render(request,"cliente/editar.html",context)