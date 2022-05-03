from django.shortcuts import render
from django.http import HttpResponse
from .models import Hilo


def inicio(request):
    return HttpResponse("Bienvenidos Colaboradores!!!!")


def buscar_team(request, team):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        hilos = Hilo.objects.filter(titulo__icontains=titulo, team=team)
        return render(request, "paginas/resultado_buscar.html", {"hilos": hilos})

    return render(request, "paginas/buscar.html")