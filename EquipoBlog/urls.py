
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginas/',include('paginas.urls')),
    path('Empleados/',include('Empleado.urls'))
]
