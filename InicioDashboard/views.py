import pdb
from django.shortcuts import redirect, render
from InicioDashboard.models import Banco, Moneda, CuentaBancaria, Cliente,Proveedor
from InicioDashboard.forms import BancoForm, MonedaForm, ClienteForm, ProveedorForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages 
from django.views import generic

# Create your views here.
def index(request):
    return render(request,"index.html")

def bienvenido(request):
    return render(request,"bienvenido.html")



