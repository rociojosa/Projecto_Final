from django.urls import path
from AppFood import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name= "Clientes"),
    path('nosotros', views.nosotros, name= "Nosotros"),
    path('cliente/<nombre>/<reserva>', views.crear_cliente, name= "CreacionCliente"),
    path('buscar_cliente', views.buscar_cliente, name= "Busqueda_cliente"),
    path('reservas', views.reservas, name="Reservas"),
    path('clientepet', views.cliente_pet, name="ClientePet"),
    path('clientes/list', views.ClienteList.as_view(), name="List"),
    path(r'^(?P<pk>\d+)$', views.ClienteDetalle.as_view(), name="Detail"),
    path(r'^nuevo$', views.ClienteCreacion .as_view(), name="New"),
    path(r'^editar/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name="Edit"),
    path(r'^borrar/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name="Delete")
]