from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from InvApp.models import Proveedor
from InvApp.serializers import ProveedorSerializer


@api_view(['GET','POST'])
def proveedor_api_view(request):

    if request.method == 'GET':
        proveedor = Proveedor.objects.all()
        proveedor_serializer = ProveedorSerializer(proveedor, many=True)
        return Response(proveedor_serializer.data)

    elif request.method== 'POST':
        proveedor_serializer = ProveedorSerializer(data=request.data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response(proveedor_serializer.data)
        return Response(proveedor_serializer.errors)




@api_view(['GET','PUT','DELETE'])
def proveedor_detail_view(request,pk=None):
    try:
        proveedor = Proveedor.objects.get(pk=pk)
    except Proveedor.DoesNotExist:
         return Response('Proveedor no encontrado',status=status.HTTP_404_NOT_FOUND) 
    if request.method=='GET':
        proveedor_serializer = ProveedorSerializer(proveedor)
        return Response(proveedor_serializer.data)

    elif request.method == 'PUT':
        proveedor_serializer = ProveedorSerializer(proveedor,data = request.data)
        if proveedor_serializer.is_valid():
            proveedor_serializer.save()
            return Response(proveedor_serializer.data)
        return Response(proveedor_serializer.errors)    

    elif request.method=='DELETE':
        proveedor.delete()
        return Response("Eliminando Proveedor")
