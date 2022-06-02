from rest_framework import serializers, exceptions

from django.contrib.auth.hashers import make_password
from django.forms import model_to_dict

from . import models


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        if self.Meta.model.objects.filter(email=attrs.get("email")).exists():
            raise exceptions.ValidationError(
                detail="User with this email already exists"
            )
        password = attrs.pop("password")
        attrs["password"] = make_password(password)
        return attrs

    class Meta:
        model = models.User
        fields = [
            "email",
            "username",
            "phone",
            "date_birth",
            "first_name",
            "second_name",
            "password",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username"]



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Profile
        fields = ["id", "slug", "user"]


class ProfileRetrieveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = models.Profile
        fields = ['id', 'username']
        lookup_field = 'slug'

    


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = "__all__"
