from rest_framework  import serializers
from .models import User
from django.contrib.auth.hashers import make_password,check_password

from rest_framework_simplejwt.tokens import AccessToken


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


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email=serializers.EmailField()
    class Meta:
        model=User
        fields=['email','password']
        
    
    def validate(self, attrs):
        email=attrs.get('email')
        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        password=attrs.get('password')
        if not check_password(password,user.password):
            raise serializers.ValidationError("Invalid email or password")

        attrs['user'] = user

        return attrs

    

    def create(self, validated_data):
        token=AccessToken()
        token['user_id']=validated_data.get('user').id
        token['role']=validated_data.get('user').role

        return str(token)

