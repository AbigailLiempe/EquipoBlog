from django.shortcuts import render, redirect
from Empleado.models import LiderDeEquipo, Colaborador, Equipo


from .forms import FormEquipo, FormLiderDeEquipo, FormLiderDeEquipo, FormColaborador, FormEquipo

def inicio(request):
      return render(request,'Empleado/Inicio.html')
def LiderNuevo(request):
      if request.method == "POST":
            mi_form = FormLiderDeEquipo(request.POST)
            if mi_form.is_valid():
                  info = mi_form.cleaned_data
                  LiderNuevo = LiderDeEquipo(nombre=info ["nombre"],
                                apellido=info["apellido"],
                                email=info["email"],
                                paginaWeb=info["paginaWeb"],
                                descripcion=info["descripcion"],
                                team =info["team"],)
                  LiderNuevo.save()
                  return redirect("Inicio Empleado")
                  
      mi_form = FormLiderDeEquipo()
      
        
      return render (request,'Empleado/formLiderDeEquipo.html',{'form': mi_form})    


def Colaborador(request):
      if request.method == "POST":
            mi_form = FormColaborador(request.POST)
            if mi_form.is_valid():
                  info = mi_form.cleaned_data
                  Colaborador = Colaborador(nombre=info ["nombre"],
                                apellido=info["apellido"],
                                email=info["email"],
                                paginaWeb=info["paginaWeb"],
                                descripcion=info["descripcion"],
                                team =info["team"],)
                  Colaborador.save()
                  return redirect("Inicio Empleado")
                  
      mi_form = FormColaborador()
      
        
      return render (request,'Empleado/formEmpleado.html',{'form': mi_form})

def Equipo(request):
      if request.method == "POST":
            mi_form = FormTeam (request.POST)
            if mi_form.is_valid():
                  info = mi_form.cleaned_data
                  Team = Team (nombre=info ["nombre"],
                               team =info["team"],)
                  Equipo.save()
                  return redirect("Inicio Empleado")
      mi_form = FormEquipo()
      
        
      return render (request,'Empleado/formEquipo.html',{'form': mi_form})
            
      