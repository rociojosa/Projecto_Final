from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField()
    alergias = forms.CharField()
    reserva = forms.IntegerField(min_value=1,max_value=200)

class ReservaClienteForm(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    horario = forms.TimeField()

class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField()

class ClientePetForm(forms.Form):
    nombre = forms.CharField()
    reserva = forms.IntegerField(min_value=1,max_value=200)
    tipo_mascota = nombre = forms.CharField()
    nombre_mascota =nombre = forms.CharField()
