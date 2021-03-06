#API

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from roominspectorapi.settings import AUTH_USER_MODEL
from django.db import models





class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name','password','username')

def validate_password(self, value):
    return make_password(value)

