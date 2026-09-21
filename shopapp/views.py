from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status

from .models import User
from .serializers import RegisterSerializer,LoginSerializer



class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializer


class LoginView(CreateAPIView):

    def post(self, request):
        ser=LoginSerializer(data=request.data)
        if ser.is_valid():
            token=ser.save()
            return Response({"access":token})
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)



    




