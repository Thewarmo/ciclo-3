from InvApp.models.clientes import Clientes
from rest_framework import serializers

class ClientesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'