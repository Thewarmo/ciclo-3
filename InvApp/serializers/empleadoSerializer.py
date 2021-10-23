from InvApp.models.empleados import Empleado
from rest_framework import serializers



class EmpleadoSErializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id_farmacia','doc_empleado','nombre','apellido']