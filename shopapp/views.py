from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from .authentication import CustomJWTAuthentication
from .permission import *
from rest_framework.viewsets import ViewSet


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


class CategoryCreateListView(ListCreateAPIView):

    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [AdminOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [AdminOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class StoreViewSet(ViewSet):
    authentication_classes=[CustomJWTAuthentication]
    permission_classes=[StorePermission]

    def create(self,request):
        ser=StoreSerializer(data=request.data)
        try:
            if ser.is_valid():
                ser.save(seller=request.user)
                return Response(ser.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
                )
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        data=Store.objects.all()
        ser=StoreSerializer(data,many=True)
        return Response(ser.data)


    def update(self,request,pk):
        obj=Store.objects.get(pk=pk)
        self.check_object_permissions(request,obj)
        ser=StoreSerializer(obj,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        obj=Store.objects.get(pk=pk)
        self.check_object_permissions(request,obj)
        ser=StoreSerializer(obj,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def destroy(self, request, pk=None):

        obj = Store.objects.get(pk=pk)

        self.check_object_permissions(request, obj)

        obj.delete()

        return Response(
            {"message": "Store deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )

    def retrieve(self, request, pk):
        obj = Store.objects.get(pk=pk)
        self.check_object_permissions(request, obj)
        ser = StoreSerializer(obj)
        return Response(ser.data)





    



    



    




