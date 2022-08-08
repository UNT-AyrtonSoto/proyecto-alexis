from django.shortcuts import redirect, render
from InicioDashboard.models import Proveedor
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages 
from django.views import generic
# Create your views here.
def index(request):
    return render(request,"index.html")

def bienvenido(request):
    return render(request,"bienvenido.html")

def listarproveedor(request):
    proveedor=Proveedor.objects.all()
    paginator = Paginator(proveedor, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"proveedor/listar.html",{'page_obj': page_obj})