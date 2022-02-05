from django.shortcuts import render
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, LogoutSerializer
from rest_framework import status, permissions, views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    @swagger_auto_schema(operation_summary="create a new user")
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginUserView(GenericAPIView):
    serializer_class = LoginSerializer

    @swagger_auto_schema(operation_summary="login user")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_200_OK)

class LogoutUserView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserListView(ListAPIView):
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()

    