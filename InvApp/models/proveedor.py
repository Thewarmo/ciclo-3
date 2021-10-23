from  django.db import models


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=60)
    direccion = models.CharField(max_length=80,null=True)
    telefono = models.BigIntegerField()

    def __str__(self):
        return f'id_proveedor : {self.id_proveedor}, nombre = {self.nombre_proveedor}, direccion = {self.direccion}, telefono = {self.telefono} '