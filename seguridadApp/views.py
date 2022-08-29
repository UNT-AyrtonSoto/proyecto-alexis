from django.shortcuts import redirect,render 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Rol , Usuario
from .forms import PasswordForm, RolForm , UsuarioForm , DatosPersonalesForm
from django.db.models import Q 

# LOGIN
def acceder(request): 
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect("bienvenido")
            else: 
                messages.error(request,"Los datos son incorrectos")         
        else: 
            messages.error(request,"Los datos son incorrectos") 

    form=AuthenticationForm() 
    return render(request,"login.html",{"form":form})
    
# Create your views here.
def salir(request):
    logout(request)
    messages.info(request,"Saliste exitosamente")
    return redirect("login")


# ROL 

def listarRol(request):
    # roles = Rol.objects.all()
    queryset=request.GET.get("buscar")
    request.user
    roles = Rol.objects.filter(eliminado=0)
    if queryset:
        roles=Rol.objects.filter(Q(descripcion__icontains=queryset)).distinct().order_by('-idRol').values() 
    paginator = Paginator(roles, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"rol/listar.html",{'page_obj': page_obj})

def agregarRol(request):
    if request.method == "POST":
        form=RolForm(request.POST)
        if form.is_valid():
            nombre_rol = form.cleaned_data.get('rol')
            # pais_banco = form.cleaned_data.get('pais')
            rol_exists = (Rol.objects.filter(rol=nombre_rol).count()>0)
            if(rol_exists):
                messages.info(request, "Rol: "+nombre_rol+", ya se encuentra registrado.")
                form=RolForm()
                context={'form':form}
                # breakpoint()
                return render(request,"rol/agregar.html",context) 
            else:
                form.save() 
                # breakpoint()
                return redirect("listarRol")           
    form=RolForm()
    context={'form':form}
    # breakpoint()
    return render(request,"rol/agregar.html",context) 

def editarRol(request,id):
    rol=Rol.objects.get(idRol=id)
    if request.method=="POST":
        form=RolForm(request.POST,instance=rol)
        if form.is_valid():
            form.save() 
            return redirect("listarRol") 
    else:
        form=RolForm(instance=rol)
        context={"form":form} 
        return render(request,"rol/editar.html",context)

def eliminarRol(request,id):
    rol =Rol.objects.get(idRol=id) 
    rol.eliminado = True
    rol.save()
    return redirect("listarRol") 

# USUARIO

def listarUsuario(request):

    queryset=request.GET.get("buscar")
    usuarios = Usuario.objects.filter(eliminado=0)
    if queryset:
        usuarios=Usuario.objects.filter(Q(descripcion__icontains=queryset)).distinct().order_by('-id').values() 
    paginator = Paginator(usuarios, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"usuario/listar.html",{'page_obj': page_obj})


def agregarUsuario(request):
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            usuario_dni = form.cleaned_data.get('dni')
            usuario_exists = (Usuario.objects.filter(dni=usuario_dni).count()>0)
            if(usuario_exists):
                messages.info(request, "Usuario con el DNI: "+usuario_dni+", ya se encuentra registrado.")
                form=UsuarioForm()
                context={'form':form}
                return render(request,"usuario/agregar.html",context) 
            else:
                form.save() 
                return redirect("listarUsuario")    
        else:
            messages.error(request, "Error en la contraseña, asegurese de cumplir con todos los requisitos")    
            form=UsuarioForm(request.POST)   
            context={'form':form}
            return render(request,"usuario/agregar.html",context) 
    form=UsuarioForm()
    context={'form':form}
    return render(request,"usuario/agregar.html",context) 

def reestablecerUsuario(request,id):
    usuario =Usuario.objects.get(id=id) 
    usuario.password = "pbkdf2_sha256$320000$hplObCJiW1aQJfmowBunST$cIXMWmTafxAxfRuQQIkDI6PRP0WhFHV1kurygHLINjY="
    usuario.save()
    return redirect("listarUsuario") 

def eliminarUsuario(request,id):
    usuario =Usuario.objects.get(id=id) 
    usuario.eliminado = True
    usuario.save()
    return redirect("listarUsuario") 


def datosPersonales(request):
    current_user = request.user
    usuario=Usuario.objects.get(id=current_user.id)
    if request.method=="POST":
        if 'DatosPersonales' in request.POST:
            form=DatosPersonalesForm(request.POST,instance=usuario)
            # print(form.errors.as_data())
            if form.is_valid():
                form.save() 
                return redirect("datosPersonales") 
            
        if 'CambioPassword' in request.POST:
            password= PasswordForm(request.POST, instance=usuario)
            if password.is_valid():
                password.save() 
                return redirect("datosPersonales") 
            else:
                messages.error(request, "Error en la contraseña, asegurese de cumplir con todos los requisitos")
                form=DatosPersonalesForm(instance=usuario)
                password=PasswordForm(request.POST,instance=usuario)
                context={"form":form , "password":password}
                return render(request,"usuario/datosPersonales.html",context) 
    else:
        form=DatosPersonalesForm(instance=usuario)
        password = PasswordForm(instance=usuario)
        context={"form":form , "password":password} 
        return render(request,"usuario/datosPersonales.html",context)