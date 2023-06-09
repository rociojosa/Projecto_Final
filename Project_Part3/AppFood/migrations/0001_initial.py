# Generated by Django 4.1.7 on 2023-03-12 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.IntegerField(unique=True)),
                ('alergias', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ClientePet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo_mascota', models.CharField(max_length=30)),
                ('nombre_mascota', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero_reserva', models.IntegerField(unique=True)),
                ('fecha', models.IntegerField(unique=True)),
                ('horario', models.IntegerField(unique=True)),
            ],
        ),
    ]
