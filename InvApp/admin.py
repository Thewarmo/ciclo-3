from django.contrib import admin
from InvApp.models.clientes import Clientes
from InvApp.models.farmacia import Farmacia
from InvApp.models.productos import Producto
from InvApp.models.empleados import Empleado
from InvApp.models.proveedor import Proveedor
from InvApp.models.clientes import Clientes

# Register your models here.

admin.site.register(Producto)
admin.site.register(Farmacia)
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Clientes)
