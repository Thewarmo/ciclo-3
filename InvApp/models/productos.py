from django.db import  models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre Producto', max_length=15)
    precio = models.IntegerField(default=0)
    proveedor = models.CharField(max_length=60)
    cantidad = models.IntegerField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return f'[id : {self.id} nombre : {self.nombre} precio: {self.precio}]'
