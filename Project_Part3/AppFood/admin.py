from django.contrib import admin

from AppFood.models import Cliente, Reservas, ClientePet

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reservas)
admin.site.register(ClientePet)