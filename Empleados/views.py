from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from Empleados.forms import EquipoFormulario, LiderFormulario, RegistroFormulario, AvatarFormulario
from Empleados.models import Equipo, Lider, Avatar, Colaborador
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate



def register(request):

    if request.method == 'POST':    

        form = RegistroFormulario(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "Empleado/inicio.html", {'mensaje':"Usuario Creado"})
    
    else:

        form = RegistroFormulario()   
    
    
    return render(request, "Empleado/registro.html", {'form':form})




def login_request(request):

    if request.method == 'POST': 

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')  
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)    

            if user:   

                login(request, user)  

                
                return render(request, "Empleados/inicio.html", {'mensaje':f"Bienvenido {user}"}) 

        else:   
            return render(request, "Empleados/inicio.html", {'mensaje':"Error. Datos incorrectos"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "Empleado/login.html", {'form':form})  



@login_required
def inicio(request):


    return render(request,"Empleado/inicio.html")

@login_required
def agregarImagen(request):

    if request.method == 'POST': 

        miFormulario = AvatarFormulario(request.POST, request.FILES) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = Avatar(user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, "Empleado/inicio.html")

    else:

        miFormulario = AvatarFormulario()
    
    return render(request, "Empleado/agregarImg.html", {'form':miFormulario})

@login_required
def agregarEquipo(request):

    
    if request.method == 'POST':    

        miFormulario = EquipoFormulario(request.POST)   

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            equipo = Equipo(nombre=informacion['equipo'], equipo=informacion['equipo'], duracion=informacion['duracion'])  

            equipo.save()

            return render(request, "Empleado/inicio.html")    

    else:

        miFormulario = EquipoFormulario()    

    dict1={"miFormulario":miFormulario}

    return render(request, "Empleado/equipo.html", dict1)

@login_required
def agregarColaborador(request):

    return render(request, "Empleado/estudiante.html")

@login_required
def agregarPosteo(request):

    return render(request, "Empleado/posteo.html")



@login_required
def agregarLider(request):


    if request.method == 'POST':   

        miFormulario = LiderFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data   
            lider = Lider(nombre=info['nombre'], apellido=info['apellido'],
            email=info['email'],area=info['Area'])

            lider.save()

            return render(request, "Empleado/inicio.html")

    else:

        miFormulario = LiderFormulario()

    dict1={'myForm':miFormulario}

    return render(request,"Empleado/lider.html", dict1)



@login_required
def busquedaEquipo(request):

    return render(request, "Empleado/busquedaEquipo.html")



@login_required
def buscar(request):


    if request.GET['equipo']:

        equipo = request.GET['equipo']      
        equipos = Equipo.objects.filter(equipo__iexact=equipo)

        return render(request, "Empleado/resultadosBusqueda.html", {"equipos":equipos, "equipo":equipo})

    else:

        respuesta="No enviaste datos."
    
    return HttpResponse(respuesta)


@login_required
def borrarLideres(request, lider_nombre):

    lider = Lider.objects.get(nombre=lider_nombre)
    
    lider.delete()
    
    lideres = Lider.objects.all()

    contexto={"lideres":lideres}

    return render(request, "Empleado/leerLideres.html",contexto)

@login_required
def editarLideres(request, lider_nombre):

    lider = Lider.objects.get(nombre=lider_nombre)

    if request.method == "POST":

        miFormulario = LiderFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            lider.nombre = informacion['nombre']
            lider.apellido = informacion['apellido']
            lider.email = informacion['email']
            lider.lidersion = informacion['area']

            lider.save()

            return render(request, "Empleado/inicio.html")

    else:

        miFormulario= LiderFormulario(initial={'nombre':lider.nombre, 'apellido':lider.apellido,
        'email':lider.email, 'lidersion':lider.lidersion})

    return render(request, "Empleado/editarLider.html",{'miFormulario':miFormulario, 'lider_nombre':lider_nombre})

@login_required
def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":   

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data    

            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "Empleado/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "Empleado/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})




@login_required

def listaLideres(request):

    lideres = Lider.objects.all() 


    contexto = {"lideres":lideres}
    return render(request, "Empleado/leerLideres.html",contexto)




class EquipoList(LoginRequiredMixin, ListView):

    model = Equipo
    template_name = "Empleado/listaEquipos.html"

class EquipoDetalle(DetailView):

    model = Equipo
    template_name = "Empleado/equipoDetalle.html"

class EquipoCreacion(CreateView):

    model = Equipo
    success_url = "/Empleado/equipo/lista"
    fields = ['nombre', 'equipo', 'duracion']

class EquipoUpdate(UpdateView):

    model = Equipo
    success_url = "/Empleado/equipo/lista"
    fields = ['nombre', 'equipo', 'duracion']


class EquipoDelete(DeleteView):

    model = Equipo
    success_url = "/Empleado/equipo/lista"


class ColaboradorList(LoginRequiredMixin, ListView):

    model = Colaborador
    template_name = "Empleado/listaColaborador.html"