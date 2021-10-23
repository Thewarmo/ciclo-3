from InvApp.models.farmacia import Farmacia
from rest_framework import serializers

class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['idFarmacia','nombre_sede','direccion','telefono','cod_sede']