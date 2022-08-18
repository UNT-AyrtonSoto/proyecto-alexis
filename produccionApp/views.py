
from django.shortcuts import render,redirect 
from .models import Trabajador
from django.db.models import Q 
from .forms import TrabajadorForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def listarTrabajador(request):   
    queryset=request.GET.get("buscar")
    trabajador=Trabajador.objects.all().order_by('-codTrabajador').values()
    if queryset:
        trabajador=Trabajador.objects.filter(Q(descripcion__icontains=queryset)).distinct().order_by('-codTrabajador').values() 
    paginator = Paginator(trabajador, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'trabajador':trabajador}
    return render(request,"listarTrabajadores.html",{'page_obj': page_obj})
def agregarTrabajador(request):
    if request.method=="POST":
        form=TrabajadorForm(request.POST)
        if form.is_valid():
            nroDocumento_trabajador=form.cleaned_data.get("nroDocumento")
            nroDocumento_exits=(Trabajador.objects.filter(nroDocumento=nroDocumento_trabajador).count()>0)
            if nroDocumento_exits:
                messages.info(request, "El Nro de documento del trabajador ya existe.")
                form=TrabajadorForm()
                context={'form':form}
                return render(request,"agregar.html",context) 
            else:
                form.save() 
                return redirect("listarTrabajador") 
    else:
        form=TrabajadorForm()
        context={'form':form} 
        return render(request,"agregar.html",context) 

def editarTrabajador(request,id):
    trabajador=Trabajador.objects.get(codTrabajador=id)
    if request.method=="POST":
        form=TrabajadorForm(request.POST,instance=trabajador)
        if form.is_valid():
            form.save() 
            return redirect("listarTrabajador") 
    else:
        form=TrabajadorForm(instance=trabajador)
        context={"form":form} 
        return render(request,"edit.html",context)

def eliminarTrabajador(request,id):
    trabajador=Trabajador.objects.get(codTrabajador=id) 
    trabajador.activo=False
    trabajador.save()
    return redirect("listarTrabajador") 