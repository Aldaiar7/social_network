from rest_framework import serializers, exceptions

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from . import models


class PostSerializer(serializers.ModelSerializer):
   class Meta:
        model = models.Post
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        if self.Meta.model.objects.filter(email=attrs.get('email')).exists():
            raise exceptions.ValidationError(
                detail="User with this email already exists"
            )
        password = attrs.pop('password')
        attrs['password'] = make_password(password)
        return attrs

    class Meta:
        model = models.User
        fields = ['email', 'username', 'phone', 'date_birth', 'first_name', 'second_name', 'password']