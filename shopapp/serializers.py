from rest_framework  import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','password']


    def validate_password(self,value):
        if len(value)<8:
            raise serializers.ValidationError("password must be 8 characters")
        return value

    def create(self, validated_data):

        data={
        "username":validated_data.get('username'),
        "email":validated_data.get('email'),
        "password":make_password(validated_data.get('password'))
        }

        user=User.objects.create(**data)
        
        return user
        

