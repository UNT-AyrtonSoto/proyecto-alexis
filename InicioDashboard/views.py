from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def listar(request):
    return render(request,"listar.html")
