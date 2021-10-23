from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from authApp.models.user import User
from authApp.serializers import UserSerializer

from authApp.serializers.userSerializer import UserSerializer

class UserCreateView(views.APIView):

    @api_view(['GET'])
    def user_api_view(request):
        if request.method == 'GET':
            user= User.objects.all()
            user_serializer = UserSerializer(user,many=True)
            return Response(user_serializer.data)

    @api_view(['GET'])
    def user_detail_view(request,username=None):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response('Usuario no encontrado',status = status.HTTP_404_NOT_FOUND)    
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)