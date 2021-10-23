from django.db import models
from django.db.models.fields import AutoField # Importe de la librería de base de datos al modelo


class Clientes(models.Model): 
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField()
    nombre = models.CharField('Nombre del cliente',max_length=60)
    apellidos = models.CharField('Apellidos del cliente',max_length=120)
    email = models.EmailField(default="No registra")
    telefono = models.BigIntegerField(null=True) 

    
    def __str__(self):
        return f'[cedula:{self.cedula}, nombre:{self.nombre}, apellidos:{self.apellidos},email:{self.email},telefono:{self.telefono}]'