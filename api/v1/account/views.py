from rest_framework import generics
from account.models import CustomUser
from . import serializers
from rest_framework import permissions, response, status
from rest_framework.views import APIView
from .. import permissions as my_permissions
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CustomUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CustomUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAdminUser]

class RegisterAPIView(APIView):
    serializer_class = serializers.RegisterSerializer
    permission_classes = [my_permissions.IsNotAuthenticated]
    def post(self, request, format = None):
        serializers = self.serializer_class(data = request.data)
        if serializers.is_valid():
            user=serializers.save()
            refresh = RefreshToken.for_user(user)
 
            response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializers.data,
                }
            return response.Response(response_data, status=status.HTTP_201_CREATED)
        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutAPIView(APIView):
    def post(self, request, format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return response.Response(status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


    
