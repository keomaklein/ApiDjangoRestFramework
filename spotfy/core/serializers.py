from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Q

from rest_framework import status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField, ValidationError, EmailField, CharField 
from rest_framework.views import APIView

from .models import Playlist

User = get_user_model()

class UserLoginSerializer(ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True, required=False)
    email = EmailField(label='Email Address', allow_blank=True, required=True)

    class Meta:
        model = User
        fields = ['username','email','password','token']

    def validate(self, data):

        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data.get("password")
        token = data.get("token")

        if not email and not username:
            raise ValidationError("Necessário informar usuário ou email!")

        user = User.objects.filter( Q(email=email) | Q(username=username) ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise  ValidationError("Usuário ou senha incorreto!")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Usuário e/ou senha incorreto(s)!")
                
        token, created = Token.objects.get_or_create(user=user_obj)
        
        if not created:        
            token.save()

        data["email"] = user_obj.email
        data["password"] = ''
        data["token"] = token.key

        return data


class UserLogoutSerializer(ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(allow_blank=True, required=False)
    email = EmailField(label='Email Address', allow_blank=True, required=True)

    class Meta:
        model = User
        fields = ['username','email','password','token']

    def logout(self, request):
        try:
            user_obj = None
            username = request.get("username")
            token_key = request.get("token")
            
            user = User.objects.filter( Q(username=username) ).distinct()

            if user.exists() and user.count() == 1:
                user_obj = user.first()
            else:
                raise ValidationError("Usuario incorreto")

            token, created = Token.objects.get_or_create(user=user_obj)

            if not created:  
                token.delete()
            else:
                raise ValidationError("Token incorreto")

        except (AttributeError, ObjectDoesNotExist):
            pass

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
