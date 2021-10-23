from django.db import models


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    doc_empleado = models.IntegerField()
    id_farmacia = models.IntegerField()
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)


    def __str__(self):
        return f'id_empleado : {self.id_empleado}, id_farmacia = {self.id_farmacia}, nombre = {self.nombre}, apellido = {self.apellido} '