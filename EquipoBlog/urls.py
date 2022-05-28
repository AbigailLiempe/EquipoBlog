
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Admin/', admin.site.urls),
    path('Paginas/',include('paginas.urls')),
    path('Empleados/',include('Empleado.urls')),
   
]
