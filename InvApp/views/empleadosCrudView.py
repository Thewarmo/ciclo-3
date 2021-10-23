from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from InvApp.models import Empleado
from InvApp.serializers import EmpleadoSErializer

@api_view(['GET','POST'])
def empleado_api_view(request):

    if request.method == 'GET':
        empleado = Empleado.objects.all()
        empleado_serializer = EmpleadoSErializer(empleado, many=True)
        return Response(empleado_serializer.data)

    elif request.method== 'POST':
        empleado_serializer = EmpleadoSErializer(data=request.data)
        if empleado_serializer.is_valid():
            empleado_serializer.save()
            return Response(empleado_serializer.data)
        return Response(empleado_serializer.errors)


@api_view(['GET','PUT','DELETE'])
def empleado_detail_view(request,pk=None):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except     Empleado.DoesNotExist:
        return Response('Empleado no encontrado',status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        empleado_serializer = EmpleadoSErializer(empleado)
        return Response(empleado_serializer.data)

    elif request.method== 'PUT':
        empleado_serializer = EmpleadoSErializer(empleado,data = request.data)
        if empleado_serializer.is_valid():
            empleado_serializer.save()
            return Response(empleado_serializer.data)
        return Response(empleado_serializer.errors)

    elif request.method== 'DELETE':
        empleado.delete()
        return Response("Eliminando Empleado")