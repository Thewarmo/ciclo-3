from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from InvApp.models import Producto
from InvApp.serializers import ProductSerializer


@api_view(['GET','POST'])
def product_api_view(request):


    if request.method == 'GET':
        product = Producto.objects.all()
        product_serializer = ProductSerializer(product,many=True)
        return Response(product_serializer.data)

    elif request.method == 'POST':
        product_serializer =   ProductSerializer(data = request.data)  
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def product_detail_view(request,pk=None):
    try:
        product = Producto.objects.get(pk=pk)
    except Producto.DoesNotExist:
         return Response('Producto no encontrado',status=status.HTTP_404_NOT_FOUND)   
    if request.method == 'GET':
        product_serializer = ProductSerializer(product)
        return Response(product_serializer.data)

    elif request.method == 'PUT':
        product_serializer = ProductSerializer(product,data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors) 

    elif request.method == 'DELETE':
        product.delete()
        return Response("Eliminado Producto...")    