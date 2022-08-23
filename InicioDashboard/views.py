import pdb
from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages 
from django.views import generic

# Create your views here.
def index(request):
    return render(request,"index.html")

def bienvenido(request):
    request.user
    return render(request,"bienvenido.html")



