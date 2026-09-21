from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import RegisterSerializer



class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializer

    



# Create your views here.
