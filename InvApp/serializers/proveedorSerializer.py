from InvApp.models.proveedor import Proveedor
from rest_framework import serializers


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id_proveedor','nombre_proveedor','direccion','telefono']