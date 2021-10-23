from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from InvApp.models import Clientes 
from InvApp.serializers import ClientesSerializer

@api_view(['GET','POST'])
def cliente_api_view(request):
    if request.method == 'GET':
        cliente = Clientes.objects.all()
        cliente_serializer = ClientesSerializer(cliente,many=True)
        return Response(cliente_serializer.data)

    elif request.method == 'POST':
        cliente_serializer = ClientesSerializer(data = request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def cliente_detail_view(request,pk=None):
    try:
        cliente = Clientes.objects.get(pk=pk)
    except Clientes.DoesNotExist:
         return Response('Cliente no encontrado',status=status.HTTP_404_NOT_FOUND)   

    if request.method =='GET':
        cliente_serializer = ClientesSerializer(cliente)
        return Response(cliente_serializer.data)
           

    elif request.method == 'PUT':
        cliente_serializer = ClientesSerializer(cliente,data = request.data)
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)

    elif request.method == 'DELETE':
        cliente.delete()
        return Response('Eliminando Cliente...')