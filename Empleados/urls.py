from django.urls import path
from Empleados.template import views
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("addEquipos/", views.agregarEquipo, name='addEquipos'),
    path("addColaborador/", views.agregarColaborador, name="addColaboradores"),
    path("addPosteo/", views.agregarPosteo, name='addPosteos'),
    path("addLider/", views.agregarLider, name='addLideres'),
    path("", views.inicio, name='Inicio'),
    path("busquedaEquipo/", views.busquedaEquipo, name="BusquedaEquipo"),
    path("buscar/", views.buscar),
    path("listaLideres", views.listaLideres, name="ListaLideres"),
    path("chauLider/<lider_nombre>", views.borrarLideres, name="BorrarLider"),
    path("editarLider/<lider_nombre>", views.editarLideres, name="EditarLider"),

    
    path('equipo/lista', views.EquipoList.as_view(), name='ListEquipos'),
    path(r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='Detail'),
    path(r'nuevo_Equipo', views.EquipoCreacion.as_view(), name='New'),
    path(r'editar_Equipo/<pk>', views.EquipoUpdate.as_view(), name='Edit'),
    path(r'borrar_Equipo/<pk>', views.EquipoDelete.as_view(), name='Delete'),

    path('Login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='Empleado/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="EditarUsuario"),

    path('colaborador/lista', views.ColaboradorList.as_view(), name='ListColaborador'),
    path('agregarImagen/', views.agregarImagen, name='Subir Avatar'),
   
]