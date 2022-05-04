from django.shortcuts import render, redirect
from Empleado.models import LeadTeam, Colaborador, Team


from .forms import FormTeamLeader, FormColaborador, FormTeam

def inicio(request):
      return render(request,'Empleado/Inicio.html')
def Lidernuevo(request):
      if request.method == "POST":
            mi_form = FormTeamLeader(request.POST)
            if mi_form.is_valid():
                  info = mi_form.cleaned_data
                  Lidernuevo = LeadTeam(nombre=info ["nombre"],
                                apellido=info["apellido"],
                                email=info["email"],
                                paginaWeb=info["paginaWeb"],
                                descripcion=info["descripcion"],
                                team =info["team"],)
                  Lidernuevo.save()
                  return redirect("Inicio Empleado")
                  
      mi_form = FormTeamLeader()
      
        
      return render (request,'Empleado/formTeamLeader.html',{'form': mi_form})    


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

def Teams(request):
      if request.method == "POST":
            mi_form = FormTeam (request.POST)
            if mi_form.is_valid():
                  info = mi_form.cleaned_data
                  Team = Team (nombre=info ["nombre"],
                               team =info["team"],)
                  Teams.save()
                  return redirect("Inicio Empleado")
      mi_form = FormTeam()
      
        
      return render (request,'Empleado/formTeams.html',{'form': mi_form})
            
      