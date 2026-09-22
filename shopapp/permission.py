from rest_framework.permissions import BasePermission
from .models import Product

class CustomerOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.role=="customer":
            return True
        return False


class ProductPermission(BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        if request.method == 'POST':
            if request.user.role == "seller":
                return True

        return False


class ProductRetrivePermission(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        if request.method in ['PUT', 'PATCH', 'DELETE']:
            if request.user.role in ['admin', 'seller']:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        
        if request.method == 'GET':
            return True

        if request.user.role == 'admin':
            return True

        if request.user.role == 'seller':
            return request.user == obj.seller

        return False

class AdminOnly(BasePermission):

    def has_permission(self, request, view):

        if request.user.role == 'admin':
            return True

        return False


class StorePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True


        if request.method=="POST":
            if request.user.role=='seller':
                return True

        

        if  request.method in ["DELETE","PUT","PATCH"]:
            if  request.user.role =="admin" or request.user.role =="seller":
                return True 

        return False

    def has_object_permission(self, request, view, obj):

        if request.method=="GET":
            return True

        if request.user.role == 'admin':
            return True

        if obj.seller == request.user :
            return True

        return False

            
        
