from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from .models import User

class CustomJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):

        auth = request.headers.get('Authorization')
        if not auth:
            raise AuthenticationFailed("need Token")
        data=auth.split()
        if len(data)<2:
            raise AuthenticationFailed("invalid token")


        if data[0].lower()!='bearer':
            raise AuthenticationFailed("invalid token")

        if not data[1]:
            raise AuthenticationFailed("invalid token")

        token=data[1]

        decoded_token = AccessToken(token)

        user_id = decoded_token["user_id"]
        role=decoded_token["role"]

        user=User.objects.get(id=user_id)

        return (user, token)





        
        

