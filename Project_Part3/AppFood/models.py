from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    alergias = models.CharField(max_length=15)
    reserva = models.IntegerField(max_length=200)

    def __str__(self):
        return f"Nombre cliente: {self.nombre}, Alergias: {self.alergias}, Reservas: {self.reserva}"


class Reservas(models.Model):
    nombre = models.CharField(max_length=30)
    reserva = models.IntegerField(max_length=200)
    fecha = models.DateField(max_length=8)
    horario = models.TimeField()

def __str__(self):
        return f"Nombre cliente: {self.nombre}, Número de reserva: {self.reserva}, fecha y horario: {self.fecha} - {self.horario}"


class ClientePet(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_mascota = models.CharField(max_length=30)
    nombre_mascota = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre Cliente Pet: {self.nombre}, Tipo de mascota: {self.tipo_mascota}, Nombre de la mascota: {self.nombre_mascota}"