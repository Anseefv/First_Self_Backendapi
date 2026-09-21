from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from .authentication import CustomJWTAuthentication
from .permission import *


from .models import User,Product
from .serializers import*



class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializer


class LoginView(CreateAPIView):

    def post(self, request):
        ser=LoginSerializer(data=request.data)
        if ser.is_valid():
            token=ser.save()
            return Response({"access":token})
        return Response (ser.errors,status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    permission_classes=[CustomerOnly]
    authentication_classes=[CustomJWTAuthentication]
    def get(self,request):
        return Response(request.user.username)



class ProductCreateListView(ListCreateAPIView):
    permission_classes=[ProductPermission]
    serializer_class=ProductSerializer
    authentication_classes=[CustomJWTAuthentication]
    queryset=Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductRetriveView(RetrieveUpdateDestroyAPIView):
    permission_classes=[ProductRetrivePermission]
    serializer_class=ProductSerializer
    authentication_classes=[CustomJWTAuthentication]
    queryset=Product.objects.all()
    



    



    



    




