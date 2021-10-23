from django.db import models


class Farmacia(models.Model):
    idFarmacia = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=45)
    cod_sede = models.CharField(max_length=45)

    def __str__(self):
        return f'id_farmacia : {self.id}, nombre_sede = {self.nombre_sede} telefono = {self.telefono}'