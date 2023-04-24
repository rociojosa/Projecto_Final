from django.shortcuts import render
from AppFood.models import Cliente, Reservas, ClientePet
from AppFood.forms import ClienteForm, BusquedaClienteForm, ReservaClienteForm, ClientePetForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.http import HttpResponse

def buscar_cliente(request):
    mi_formulario = BusquedaClienteForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        clientes_filtrados = Cliente.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "clientes": clientes_filtrados,
        }
        return render(request, "AppFood/busqueda_cliente.html", context=context)
    else:

        mi_formulario =BusquedaClienteForm()

        return render(request,"AppFood/busqueda_cliente.html", {"mi_formulario":mi_formulario})


def inicio(request):
    return render(request, "AppFood/inicio.html")

def clientes(request):
    if request.method == "POST":
        mi_formulario = ClienteForm(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente_save = Cliente(
                nombre=informacion['nombre'],
                alergias = informacion['alergias'],
                reserva = informacion['reserva'],
              )
            
            cliente_save.save()
    all_clientes = Cliente.objects.all()
    context = {
        "clientes": all_clientes,
        "form": ClienteForm(),
        "form_busqueda": BusquedaClienteForm(),
    }

    return render(request, "AppFood/cliente.html", context=context)


def crear_cliente(request, nombre, alergias, reserva):
    cliente_save= Cliente( nombre=nombre , alergia=alergias , reserva=int(reserva))
    cliente_save.save()
    context = {
        "Nombre": nombre , "Reserva": reserva, "Alergias": alergias
    }
    return render(request, "AppFood/cliente_save.html", context=context)


def nosotros(request):
    return render(request, "AppFood/nosotros.html")

def reservas(request):
    if request.method == "POST":
        mi_formulario = ReservaClienteForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            reserva_save = Reservas(
                nombre= informacion['nombre'],
                fecha = informacion['fecha'],
                horario = informacion['horario'],
              )
            
            reserva_save.save()

    all_reservas =Reservas.objects.all()
    context = {
        "nombre": all_reservas,
        "form_reserva": ReservaClienteForm(),
    }
    return render(request, "AppFood/reservas.html", context)


def cliente_pet(request):
    if request.method == "POST":
        mi_formulario = ClientePetForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            clientepet_save = ClientePet(
                nombre = informacion['nombre'],
                tipo_mascota = informacion['tipo_mascota'],
                nombre_mascota = informacion ['nombre_mascota'],
              )
            
            clientepet_save.save()

    all_clientespet =ClientePet.objects.all()
    context = {
        "nombre": all_clientespet,
        "mi_formulario": ClientePetForm(),
    }

    return render(request, "AppFood/clientepet.html", context=context)

class ClienteList(ListView):
    model = Cliente
    template_name = "AppFood/cliente_list.html"

class ClienteDetalle(DetailView):
    model = Cliente
    template_name = "AppFood/cliente_detalle.html"

class ClienteCreacion(CreateView):
    model = Cliente
    sucess_url = "/AppFood/clientes/list"
    fields = ['nombre', 'reservas']

class ClienteUpdate(UpdateView):
    model = Cliente
    sucess_url = "/AppFood/clientes/list"
    fields = ['nombre', 'reservas']

class ClienteDelete(DeleteView):
    model = Cliente
    sucess_url = "/AppFood/clientes/list"