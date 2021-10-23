from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from InvApp.models import Farmacia
from InvApp.models.empleados import Empleado
from InvApp.serializers import FarmaciaSerializer

@api_view(['GET','POST'])
def farmacia_api_view(request):

    if request.method == 'GET':
        farmacia = Farmacia.objects.all()
        farmacia_serializer = FarmaciaSerializer(farmacia, many=True)
        return Response(farmacia_serializer.data)

    elif request.method== 'POST':
        farmacia_serializer = FarmaciaSerializer(data=request.data)
        if farmacia_serializer.is_valid():
            farmacia_serializer.save()
            return Response(farmacia_serializer.data)
        return Response(farmacia_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def farmacia_detail_view(request,pk=None):
    try:
        farmacia = Farmacia.objects.get(pk=pk)
    except Farmacia.DoesNotExist:
        return Response('Farmacia no encontrada',status=status.HTTP_404_NOT_FOUND)    
    if request.method == 'GET':
        farmacia_serializer = FarmaciaSerializer(farmacia)
        return Response(farmacia_serializer.data)

    elif request.method == 'PUT':
        farmacia_serializer = FarmaciaSerializer(farmacia,data = request.data)
        if farmacia_serializer.is_valid():
            farmacia_serializer.save()
            return Response(farmacia_serializer.data)
        return Response(farmacia_serializer.errors)    

    elif request.method=='DELETE':
        farmacia.delete()
        return Response("Eliminando Farmacia...")


