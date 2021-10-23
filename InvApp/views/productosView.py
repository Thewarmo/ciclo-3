from rest_framework import generics,status
from rest_framework.response import Response
from InvApp.models.productos import Producto
from InvApp.serializers.productoSerializer import ProductSerializer

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Producto.objects.all()