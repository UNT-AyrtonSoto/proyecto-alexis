from decimal import Decimal
import json
import pdb
from django.shortcuts import render, redirect
from .forms import BancoForm, MonedaForm, ClienteForm, PedidoForm
from .models import Banco, DetallePedido, Moneda, Cliente, Pedido
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
    
#PEDIDOS
def listarPedidos(request):
    pedidos = Pedido.objects.filter(eliminado=False)
    paginator = Paginator(pedidos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"pedidos/listar.html",{'page_obj': page_obj})

def agregarPedido(request):
    form = PedidoForm()
    if request.method=="POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            fechaEntrega = form.cleaned_data.get('fechaEntrega')
            estado = form.cleaned_data.get('estado')
            documentoCliente = form.cleaned_data.get('documentoIdentidad')
            nombreCliente = form.cleaned_data.get('nombres')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            
            # breakpoint()
            
            pedido = Pedido()
            pedido.fechaEntrega = fechaEntrega
            pedido.estado = estado
            pedido.documentoCliente = documentoCliente
            pedido.nombreCliente = nombreCliente
            # breakpoint()
            
            pedido.save()
            
            for detalle in detalleJSON:
                tempDetalle = DetallePedido(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],codPedido=pedido)
                tempDetalle.save()
            return redirect('listarPedidos')    
        else:
            form = PedidoForm()
    context = {'form':form}
    return render(request,"pedidos/agregar.html",context)     

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

def editarPedido(request,id):
    pedido = Pedido.objects.get(codPedido=id)
    detalle = DetallePedido.objects.filter(codPedido=id).values('codPedido','codDetallePedido','descripcion','cantidad','eliminado')
    # strDetalle = serializers.serialize("json",list(detalle),fields={'descripcion'})
    strDetalle = json.dumps([dict(item) for item in detalle], cls=DecimalEncoder)
    if request.method=="POST":
        form=PedidoForm(request.POST)
        if form.is_valid():
            documentoCliente = form.cleaned_data.get('documentoIdentidad')
            nombres = form.cleaned_data.get('nombres')
            fechaEntrega = form.cleaned_data.get('fechaEntrega')
            estado = form.cleaned_data.get('estado')
            detalleSTR = form.cleaned_data.get('detalle')
            
            # breakpoint()
            detalleJSON = json.loads(detalleSTR)
            
            # breakpoint()
            
            pedido.fechaEntrega = fechaEntrega
            pedido.documentoCliente = documentoCliente
            pedido.nombreCliente = nombres
            pedido.estado = estado
            # breakpoint()
            pedido.save()
            
            for detalle in detalleJSON:
                if(detalle['codDetalleOrdenCompra']==0):
                    tempDetalle = DetallePedido(descripcion=detalle['descripcion'],cantidad=detalle['cantidad'],codPedido=pedido, eliminado=0)
                    tempDetalle.save()
                else:
                    tempDetalle = DetallePedido.objects.get(codDetallePedido=detalle['codDetallePedido'])
                    tempDetalle.descripcion=detalle['descripcion']
                    tempDetalle.cantidad=detalle['cantidad']
                    tempDetalle.eliminado=detalle['eliminado']
                    tempDetalle.save()
            return redirect('listarOrdenesCompra')    
    else:
        
        initial_dic = {
            'documentoIdentidad': pedido.codTrabajador,
            'nombres': pedido.codProveedor,
            'igv': pedido.igv,
            'fecha': pedido.fecha,
            'descuento': pedido.descuento,
            'estado': pedido.estado,
            'observaciones': pedido.observaciones,
            'detalle': strDetalle,
        }
        
        form=PedidoForm(request.POST or None, initial=initial_dic)
        context={"form":form, "detalle": detalle}
        return render(request, "ordenCompra/editar.html",context)

def eliminarPedido(request,id):
    ordencompra = Pedido.objects.get(codOrdenCompra=id)
    ordencompra.eliminado = True
    ordencompra.save()
    return redirect("listarOrdenesCompra")
